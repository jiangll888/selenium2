import os
from PIL import Image
import docx
from docx.opc.exceptions import PackageNotFoundError
from mutagen import MutagenError
from mutagen.mp3 import MP3
from config import settings
import cv2
from log.log_record import LogRecord

class OperaFile:
    def __init__(self,filename,file_type,logger):
        self.filename = filename
        self.file_type = file_type
        self.logger = logger

    def get_filename(self):
        filename = self.filename.split("\\")[-1]
        filename = settings.DOWNLOAD_PATH + "\\" + filename
        return filename

    def check_file_status(self):
        filename =  self.get_filename()
        try:
            if self.file_type == "pic":
                with Image.open(filename) as fp:
                    if fp.size:
                        self.logger.info("{} 文件已找到".format(filename))
                        return True
            elif self.file_type == "doc":
                fp = docx.Document(filename)
                if len(fp.paragraphs):
                    self.logger.info("{} 文件已找到".format(filename))
                    return True
            elif self.file_type == "video":
                fp = cv2.VideoCapture(filename)
                video_status = fp.isOpened()
                fp.release()
                if video_status:
                    self.logger.info("{} 文件已找到".format(filename))
                    return True
                else:
                    self.logger.warning("{} 文件不存在".format(filename))
                    return False
            else:
                audio = MP3(filename)
                if audio.info.length:
                    self.logger.info("{} 文件已找到".format(filename))
                    return True
        except (FileNotFoundError,PackageNotFoundError,MutagenError) as e:
            self.logger.warning("{} 文件不存在".format(filename))
            self.logger.warning(e)
            return False

    def delete_file(self):
        filename = self.get_filename()
        if self.check_file_status():
            os.remove(filename)
            self.logger.info("{} 文件已删除".format(filename))