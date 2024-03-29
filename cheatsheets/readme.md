# Useful Cheatsheets :page_facing_up:

 * Bash - <a href="https://devhints.io/bash" target="_blank">cheatsheet</a>
 * radare2 - <a href="https://book.rada.re/" target="_blank">cheatsheet</a>
 * BinaryNinja - <a href="https://cheatography.com/watbulb/cheat-sheets/binary-ninja-macos/" target="_blank">cheatsheet</a>
 * awk - <a href="https://www.shortcutfoo.com/app/dojos/awk/cheatsheet" target="_blank">cheatsheet</a>
 * sed - <a href="https://quickref.me/sed" target="_blank">cheatsheet</a>
 * dd - <a href="https://www.jamescoyle.net/cheat-sheets/1012-dd-cheat-sheet" target="_blank">cheatsheet</a> 
 * Regex - <a href="https://quickref.me/regex" target="_blank">cheatsheet</a>
 * Docker - <a href="https://quickref.me/docker" target="_blank">cheatsheet</a>
 * Dockerfile - <a href="https://lzone.de/cheat-sheet/Dockerfile" target="_blank">cheatsheet</a>
 * Markdown - <a href="https://readme.directual.com/data/data-types/markdown-cheatsheet" target="_blank">cheatsheet</a>



**Self sign certificate**:

  generating private 2048-RSA key:
  `openssl genrsa -out priv.key 2048`

  generating certificate signed request:
  `openssl req -new -key priv.key -out request.csr`

  generating certificate:
  `openssl x509 -req -days 90 -in request.csr -signkey priv.key -out cert.crt`
