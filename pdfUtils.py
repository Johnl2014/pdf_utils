from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

def extract(filename, *pageNumbers):
    """Extract selected pages from a PDF file.

    Parameters
    ----------
    filename: string
        filename of the pdf file to extract pages from, e.g. 'my file.pdf'.
    pageNumbers: variable number of ints
        page numbers in the original pdf to extract.

    Output
    ------
    A new pdf file with only extracted pages in the same directory as the input file.
    The output file has a filename being the input filename appended "-extracted",
    e.g. 'my file-extracted.pdf'.
    """
    if not (filename and pageNumbers):
        print("Must specify both a filename and page numbers to extract!")
        return
    inputpdf = PdfFileReader(open(filename, "rb"))
    output = PdfFileWriter()
    for i in pageNumbers:
        output.addPage(inputpdf.getPage(i-1))
    with open(filename[:filename.index('.')] + "-extracted.pdf", "wb") as outputStream:
        output.write(outputStream)

def merge(*filenames):
    """Merge multiple PDF files into a single PDF file.

    Parameters
    ----------
    filenames: variable number of strings
        filenames of the pdf files to merge, e.g. 'file1.pdf', 'file2.pdf'.
    
    Output
    ------
    A new pdf combining input files in the same directory as the first input file.
    The output file has a filename being the first input filename appended "-merged",
    e.g. 'file1-merged.pdf'.
    """
    if not filenames:
        print("Must specify at least one pdf filename!")
        return
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    with open(filenames[0][:filenames[0].index('.')] + "-merged.pdf", "wb") as outputStream:
        merger.write(outputStream)
    merger.close()