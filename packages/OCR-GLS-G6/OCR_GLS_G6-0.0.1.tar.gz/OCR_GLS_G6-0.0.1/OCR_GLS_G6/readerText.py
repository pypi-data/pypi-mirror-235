# -*- coding: utf-8 -*-

#readerText.py

from ironpdf import *

class readerText :
      def __init__(self, pdfPath):
        self.pdfPath = pdfPath
        
      def pdfToImg(self, fileName, fileType="png"):
            pdf = PdfDocument.FromFile(self.pdfPath)
            # Extract all pages to a folder as image files
            pdf.RasterizeToImageFiles(fileName+"."+fileType,DPI=300)
            return fileName+"."+fileType