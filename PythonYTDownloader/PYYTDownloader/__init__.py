from pytube import YouTube as __YouTube, Playlist as __Playlist
from pytube.cli import on_progress as __on_progress
import os as __os, requests as __requests

# Exceptions Classes
class DownloaderExceptions(Exception):
    def __init__(self):
        print('Exception: DownloaderException')
class VideoUrlException(DownloaderExceptions):
    def __init__(self, message):
        self.__message = str(message).capitalize()
    def __str__(self):
        return "VideoUrlException: {}".format(self.__message)
class VideoFormatError(DownloaderExceptions):
    def __init__(self, message):
        self.__message = str(message).capitalize()
    def __str__(self):
        return 'VideoFormatError: {}'.format(self.__message)
class VideoExistError(DownloaderExceptions):
    def __init__(self, message):
        self.__message = str(message).capitalize()
    def __str__(self):
        return 'VideoFormatError: {}'.format(self.__message)
class VideoSrcTypeError(DownloaderExceptions):
    def __init__(self, message):
        self.__message = str(message).capitalize()
    def __str__(self):
        return 'VideoSrcType: {}'.format(self.__message)

# On Complete Print Check Sign
def __on_complete():
    "Don't Use this, throws error"
    try:
        print(u'\u2713')
    except UnicodeError:
        print("@")
def __getVideoUrl(topic):
    "Don't Use this, throws error"
    url = 'https://www.youtube.com/results?q=' + topic
    count = 0
    cont = __requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count+=1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
    if lst[count-5] == "/results":
        try:
            raise VideoExistError("No Video Found with that name")
        except VideoExistError as e:
            print(e)
            return False
    return "https://www.youtube.com"+lst[count-5]

def __checkExistence(name, path, **kargs):
    "Don't Use this, throws error"
    unwanted = ['/', '\\', '*', ':', '?', '"', '<', '>', '|', '#']
    name = str(name)+str(".mp3")
    cbType = kargs.get('get', '__default')
    for item in unwanted:
        if item in name:
            name = name.replace(item, '')
    path = __os.path.join(path, 'Music')
    if cbType == '__default':
        return __os.path.exists(__os.path.join(path, name))
    else:
        return name
def __rename(direc):
    "Don't Use this, throws error"
    direc = direc.replace('/', '\\')
    source = direc
    direc = direc.replace(".mp4", ".mp3")
    path = direc
    try:
        __os.rename(source, path)
        __on_complete()
    except FileExistsError:
        print("\nFile Already Exist")
def __downloader(video_url, vformat, **kargs):
    takenPath = kargs.get('path', '__default')
    if takenPath == '__default':
        takenPath = __os.environ.get('USERPROFILE')
    tempPath = kargs.get('tempPath')
    if video_url == '':
        try:
            raise VideoUrlException("Video URL cannot be Empty String")
        except VideoUrlException as e:
            print(e)
            return False
    elif video_url == None:
        try:
            raise VideoUrlException('Video URL cannot be of NoneType')
        except VideoUrlException as e:
            print(e)
            return False
    else:
        vformat = vformat.lower()
        if vformat != 'video' or vformat != 'audio':
            ytd = __YouTube(video_url, on_progress_callback=__on_progress)
            video_title = ytd.title
            if vformat == 'audio':
                path_ = __os.path.join(takenPath, 'Music')
                if tempPath != False:
                    path_ = __os.path.join(path_, tempPath)
                if kargs.get('type'):
                    result = __checkExistence(video_title, path_, get='playlist')
                else:
                    result = __checkExistence(video_title, path_)
                if result == True:
                    print("Audio \"{}\"\nAlready Exist in \"{}\\Music\"\nTry Changing Path, if you wanna download anyway".format(video_title, takenPath))
                    return False
                elif result == False:
                    print("Downloading Audio {}.mp3\n".format(video_title), end='')
                    cb = ytd.streams.get_audio_only().download(f"{path_}\\Music")
                    ytd.register_on_complete_callback(__rename(cb))
                    return True
                else:
                    return result
            else:
                path_ = __os.path.join(takenPath, 'Videos')
                if tempPath != False:
                    path_ = __os.path.join(path_, tempPath)
                    
                if kargs.get('type'):
                    result = __checkExistence(video_title, path_, get='playlist')
                else:
                    result = __checkExistence(video_title, path_)
                if result == True:
                    print("Video \"{}\"\nAlready Exist in \"{}\\Videos\"\nTry Changing Path, if you wanna download anyway".format(video_title, path_))
                    return False
                elif result == False:
                    print("Downloading Video {}.mp4\n".format(ytd.title), end='')

                    ytd.streams.get_highest_resolution().download(path_)
                    ytd.register_on_complete_callback(__on_complete())
                    return True
                else:
                    return result
        else:
            try:
                raise VideoFormatError("Only Audio or Video format allowed")
            except VideoFormatError as e:
                print(e)
                return False
def ytdownload(video_url, vformat, **kargs):
    """
    Download YouTube Video in Audio or Video Formate as Specified
    Takes Two Positional Arguments and one Optional Arguments
    1. video_url
        It is a Actual Video URL from YouTube. It may either be URL of
        Single Video or PlayList
    2. vformat
        It is a Format in which download should be taken place
        'audio' for Audio and 'video' for Video
    3. path='PATH'
        It is optional.
        It specifies where the files should be downloaded.
        By Default
            it stores in USERPROFILE/Musics for Audio and /Videos for Videos
        But by providing argument as
            path='certain_path' video or audio will be downloaded in certain_path
    eg:
    ytdownload(video_url, 'audio', path='C:/Users/root/Musics')
    """#.format(os.environ.get('USERPROFILE'), os.environ.get('USERPROFILE'))
    path = kargs.get('path', '__default')
    video_src_type = ''
    if str(video_url).startswith('https://www.youtube.com'):
        if str(video_url).startswith('https://www.youtube.com/playlist'):
            video_src_type = 'playlist'
        else:
            video_src_type = 'single'
    else:
        video_src_type = 'name'
    if video_url == '' or None:
        try:
            raise VideoUrlException('Empty string or NoneType is not acceptable as VideoUrl')
        except VideoUrlException as e:
            print(e)
            return False
    else:
        if video_src_type == 'name':
            url = __getVideoUrl(video_url)
            if vformat == 'video':
                if __downloader(url, 'video', path=path):
                    return True
                else:
                    return False
            elif vformat == 'audio':
                if __downloader(url, 'audio', path=path):
                    return True
                else:
                    return False
            else:
                try:
                    raise VideoFormatError('Only Audio or Video format in allowed')
                except VideoFormatError as e:
                    print(e)
                    return False
        elif video_src_type == 'single':
            if vformat == 'video':
                if __downloader(video_url, 'video', path=path):
                    return True
                else:
                    return False
            elif vformat == 'audio':
                if __downloader(video_url, 'audio', path=path):
                    return True
                else:
                    return False
            else:
                try:
                    raise VideoFormatError('Only Audio or Video format in allowed')
                except VideoFormatError as e:
                    print(e)
                    return False
        elif video_src_type == 'playlist':
            plist = __Playlist(video_url)
            get_url = plist.video_urls
            if vformat == 'video':
                for item in get_url:
                    if __downloader(item, 'video', path=path, tempPath = plist.title):
                        pass
                    else:
                        return False
                else:
                    return False
            elif vformat == 'audio':
                collection = []
                for item in get_url:
                    result = __downloader(item, 'audio', path=path, tempPath = plist.title)
                    if result:
                        pass
                    else:
                        collection.append(result)
                for item in collection:
                    if item == False:
                        return False
                    else:
                        return True
                else:
                    return False
            else:
                try:
                    raise VideoFormatError('Only Audio or Video format in allowed')
                except VideoFormatError as e:
                    print(e)
                    return False
        else:
            try:
                raise VideoSrcTypeError('VideoSrcType Error: Only YouTube video can be downloaded')
            except VideoSrcTypeError as e:
                print(e)
                return False