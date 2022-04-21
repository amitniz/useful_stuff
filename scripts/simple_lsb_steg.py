from PIL import Image
import argparse




def _text2bin(text):
    '''converts a string to a list of binary numbers'''

    bin_list = []
    for c in text:
        bin_list+= list('{:08b}'.format(ord(c) if type(c) == str else c))
    return [int(c) for c in bin_list]

def _bin2text(list):
    '''converts a list of binary numbers to a string'''
    return b''.join([(int(''.join([str(i) for i in list[i:i+8]]),2)).to_bytes(1,'big') for i in range(0,len(list),8)])

def _lsb_pixel_inject(pix, bit,channel):
    '''gets a pixel, a bit value and a color channel and returns a modified pixel for the lsb steg.'''
    if type(pix) == int:
        return (pix & 0xFE) | bit
    else:
        if channel == 'red':
            return ((pix[0] & 0xFE) | bit,pix[1],pix[2])
        elif channel =='green':
            return (pix[0],(pix[1] & 0xFE) | bit,pix[2])
        else:
            return (pix[0],pix[1],(pix[2] & 0xFE) | bit)

def _lsb_pixel_extract(pix,channel):
    if type(pix) == int:
        return pix & 1 
    else:
        if channel == 'red':
            return pix[0] & 1
        elif channel =='green':
            return pix[1] & 1
        else:
            return pix[2] & 1


def hide_message(img,msg,channel):
    bin_msg = [int(c) for c in _text2bin(msg)]
    for y in range(img.height):
        for x in range(img.width):
            pix = img.getpixel((x,y))
            val = bin_msg[img.width*y+x] if len(bin_msg) > img.width*y+x else 0
            img.putpixel((x,y),_lsb_pixel_inject(pix,val,channel))




def extract_message(img,channel):
    bin_list =[]
    for y in range(img.height):
        for x in range(img.width):
            pix = img.getpixel((x,y))
            bin_list.append(_lsb_pixel_extract(pix,channel))
    
    return _bin2text(bin_list)








if __name__ == '__main__':

    # ------------------------------------------ Setup -------------------------------------
    parser = argparse.ArgumentParser(description="Simple lsb stegnography")
    parser.add_argument('--input','-i',type=str,metavar='IMAGE', help="input image",required=True)
    parser.add_argument('--output','-o',type=str,metavar='OUTFILE',help="output file")
    parser.add_argument('--file','-f',type=str,metavar='file',help="the file to hide")
    parser.add_argument('--channel','-c',type=str,default='blue',metavar='RED|GREEN|BLUE',help="the hidden message channel")
    parser.add_argument('--extract','-e',action='store_true',help="extract mode")

    args = parser.parse_args()

    try:
        img = Image.open(args.input)

    except:
        print("[!] Can't open the given image.")
        exit(1)


    channel = args.channel.lower()
    if channel not in ['red','green','blue']:
        print("[!] Invalid Channel.")
        exit(1)


# ------------------------------------------------------------------------------------------


    if args.extract: #extract mode
        msg = extract_message(img,args.channel)
        
        if args.output:
            with open(args.output,'wb') as f:
                f.write(msg)
        else:
            print(msg)
    
    else: #inject mode
        if not args.output:
            print("[!] Output file is missing.")
            exit(1)

        if args.file: #read from agruments
            with open(args.file,'rb') as f:
                msg = f.read()
        
        else:
            msg = input("Insert the message:")
            print(msg)

        hide_message(img,msg,channel)
        try:
            img.save(args.output)
        except:
            print("[!] Couldn't save the file.")
            exit(1)

