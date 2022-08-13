# 从YouTube下载资源的方法

from pytube import Playlist, YouTube
from pytube.cli import on_progress
import os
import ffmpeg


# 从播放列表下载音频并保存为MP3


def down_mp3_from_playlist():
    path = "D:\\m"
    url = str(input('请输入或粘贴您要下载的播放列表网址: \n>>'))
    print('请输入您要保存的路径(留空表示保存到当前路径)')
    des = str(input('>> ')) or '.'
    p = Playlist(url)
    for url in p.video_urls:
        yt = YouTube(url, on_progress_callback=on_progress)
        vd = yt.streams.filter(only_audio=True).first()
        out_file = vd.download(os.path.join(path, des))
        base, ext = os.path.splitext(out_file)
        new_file = base+'.mp3'
        os.rename(out_file, new_file)
        print(yt.title+'下载完成')

# 从播放列表下载视频


def down_video_from_playlist():
    url = str(input('请输入或粘贴您要下载的播放列表网址: \n>>'))
    path = "D:\\m"
    p = Playlist(url)
    for i in range(len(p.video_urls)):
        yt = YouTube(p.video_urls[i], on_progress_callback=on_progress)
        st = yt.streams.filter(resolution='1080p').first()
        ad = yt.streams.filter(only_audio=True).first()
        st.download(path, f'v{i}.mp4')
        ad.download(path, f'a{i}.mp4')
        print('下载完成,开始合并数据')
        v = ffmpeg.input(os.path.join(path, f'v{i}.mp4'))
        a = ffmpeg.input(os.path.join(path, f'a{i}.mp4'))
        ffmpeg.concat(v, a, v=1, a=1).output(
            os.path.join(path, f'{i}.mp4')).run()

    print('complate all')

# 下载单个视频


def down_video():
    path = "D:\\m"
    url = str(input('请输入或粘贴您要下载的播放列表网址: \n>>'))
    yt = YouTube(url, on_progress_callback=on_progress)
    sv = yt.streams.filter(resolution='1080p').first()
    sa = yt.streams.filter(only_audio=True).first()
    sv.download(path, 'v.mp4')
    sa.download(path, 'a.mp4')
    v = ffmpeg.input(os.path.join(path, 'v.mp4'))
    a = ffmpeg.input(os.path.join(path, 'a.mp4'))
    file_name = yt.title.replace(' ', '')
    ffmpeg.concat(v, a, v=1, a=1).output(
        os.path.join(path, 'output.mp4')).run()
    # print(yt.title.split('|')[0])


# 下载单个音频

def down_audio():
    path = "D:\\m"
    url = str(input('请输入或粘贴您要下载的播放列表网址: \n>>'))
    yt = YouTube(url, on_progress_callback=on_progress)
    ad = yt.streams.filter(only_audio=True).first()
    out_file = ad.download(path)
    base, ext = os.path.splitext(out_file)
    new_file = base+'.mp3'
    os.rename(out_file, new_file)
    print('完成任务!')


if __name__ == "__main__":
    print('您是要进行什么操作呢?(输入对应的数字即可) \n 1.从播放列表下载视频 \n 2.从播放列表下载音频 \n 3.下载单个视频 \n 4.下载单个音频 \n')
    idx = int(input('...'))
    print(idx)
    match idx:
        case 1:
            down_video_from_playlist()
        case 2:
            down_mp3_from_playlist()
        case 3:
            down_video()
        case 4:
            down_audio()
        case _:
            print('请选择有效的功能选项')

    # path="\\m"
    # a = ffmpeg.input(os.path.join(path, 'a.mp4'))
    # print(a)
