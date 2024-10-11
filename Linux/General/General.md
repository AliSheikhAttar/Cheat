# General
[Partitioning](./Partitioning.md)

## Gui
```bash
echo $XDG_CURRENT_DESKTOP
env | grep XDG_CURRENT_DESKTOP
```

## ScreenShot
    - X window and save <image.jpg> in Home dir
    ```bash
    import <image.jpg>
    ```

    - X window and save it in the Encapsulated PostScript format to include in another document

    ```bash
    import <figure.eps>
    ```
    - entire X server screen and save root.jpg

    ```bash
    import -window root <root.jpg>
    ```
    - capture the 512x256 area at the upper right corner of the X server screen in the PNG image format in a well-compressed file entitled corner.png, without using the mouse
    ```bash
    import -window root -crop <512x256-0-0> -gravity <northeast> -quality 90 <corner.png>
    ```

## Video
- install ffmpeg
```bash
    sudo apt-get install ffmpeg
Summary
Here are some recommended FFmpeg commands based on your needs:

H.265 encoding (efficient compression):
bash
Copy code
ffmpeg -i input.mp4 -c:v libx265 -crf 28 -c:a copy output.mp4
H.264 with variable bitrate (good balance):
bash
Copy code
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset slow -c:a copy output.mp4
Reduce bitrate:
bash
Copy code
ffmpeg -i input.mp4 -b:v 1000k -c:a copy output.mp4
Downscale resolution:
bash
Copy code
ffmpeg -i input.mp4 -vf scale=1280:720 -c:a copy output.mp4
By tweaking these parameters, you can achieve the best trade-off between video size and quality.
```

## Live watch
```bash
watch -n1 date +%r
```

## encode
- base64
```bash
base64 inputfile > encodedfile
```
- openssl
```bash
base64 inputfile > encodedfile
```

## decode
- base64
```bash
base64 --decode encodedfile > decodedfile
```
- openssl
```bash
openssl enc -aes-256-cbc -d -in encryptedfile -out decryptedfile
```
