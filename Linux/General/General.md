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
```
- Compress
```bash
    ffmpeg -i big_buck_bunny.y4m -vcodec libx265 -crf 28 fps-fps=30 big_buck_bunny.mp4
```
- Change format
```bash
    ffmpeg -i inputfile.video outputfile.video
```

## Live watch
```bash
watch -n1 date +%r
```

