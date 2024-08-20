MIME | Multipurpose Internet Mail Extensions type
MIME = Primary Type/Sub-Type


- [x] [Starting a New Digital Forensic Investigation Case in Autopsy 4.19+](https://www.youtube.com/watch?v=fEqx0MeCCHg&t=123s)


To open a file: MacOS and Linux use the _file header_, Windows uses _file extension_ -[source](https://youtu.be/fEqx0MeCCHg?t=905)

`file -i file.type` gives  MIME type and encoding details

`xxd file.txt | head` head of hex dump format to find signature in hex (byte offset = 0)
