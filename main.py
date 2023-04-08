import os
import io
from PyPDF2 import PdfReader, PdfMerger

import warnings
warnings.filterwarnings('ignore')

def find_pdfs(directory):
    """
    Find all PDF files in a given directory.

    Args:
        directory (str): The directory to search for PDF files.

    Returns:
        A list of file paths for all PDF files in the directory.
    """
    # create a list to store the PDF files
    pdf_files = []
    
    # loop through the directory and find all PDF files
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            pdf_files.append(os.path.join(directory, filename))
            
    return pdf_files

def merge_pdfs(pdf_file_list, target_directory, master_file_name):
    """
    Merge a list of PDF files into a single PDF.

    Args:
        pdf_file_list (list): A list of file paths for the PDF files to merge.
        target_directory (str): The directory to save the merged PDF to.
        master_file_name (str): The name to use for the merged PDF file.

    Returns:
        None
    """
    # create a PDF merger object
    pdf_merger = PdfMerger()

    # loop through each PDF file and add its pages to the merger object
    for pdf_file in pdf_file_list:
        with open(pdf_file, 'rb') as f:
            pdf_reader = PdfReader(f)
            pdf_merger.append(pdf_reader)

    # write the combined PDF to a file
    save_location = os.path.join(target_directory, master_file_name)
    with open(save_location, 'wb') as f:
        pdf_merger.write(f)

def pdf_to_text(pdf_file_path, target_directory, txt_file_name):
    """
    Convert a PDF file to a text file.

    Args:
        pdf_file_path (str): The path to the PDF file to convert.
        target_directory (str): The directory to save the text file to.
        txt_file_name (str): The name to use for the text file.

    Returns:
        None
    """
    with open(pdf_file_path, 'rb') as f:
        pdf_reader = PdfReader(f)
        output_string = io.StringIO()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            output_string.write(page.extract_text())
            
    save_location = os.path.join(target_directory, txt_file_name)      

    with open(save_location, 'w', encoding='utf-8') as f:
        f.write(output_string.getvalue())

def main(find_pdfs_directory=os.getcwd(), merge_pdf_directory=os.getcwd(), merge_pdf_file_name='Merged_PDFs.pdf', merge_text_directory=os.getcwd(), merge_text_file_name='Scraped_PDFs_to_Text.txt', merge_pdfs_bool=True, merge_pdf_to_text_bool=True):
    """
    The main function that calls the other functions to find, merge and convert PDF files.

    Args:
        find_pdfs_directory (str): The directory to search for PDF files. Default is the current working directory.
        merge_pdf_directory (str): The directory to save the merged PDF to. Default is the current working directory.
        merge_pdf_file_name (str): The name to use for the merged PDF file. Default is 'Merged_PDFs.pdf'.
        merge_text_directory (str): The directory to save the text file to. Default is the current working directory.
        merge_text_file_name (str): The name to use for the text file. Default is 'Scraped_PDFs_to_Text.txt'.
        merge_pdfs_bool (bool): Whether or not to merge the PDF files. Default is True.
            If set to False, the PDF files will not be merged.
        merge_pdf_to_text_bool (bool): Whether or not to convert the merged PDF to text. Default is True.
            If set to False, the merged PDF will not be converted to text.

    Returns:
        None
    """
    pdf_list = find_pdfs(find_pdfs_directory)
    print(f"PDF files found {pdf_list}")

    if merge_pdfs_bool:
        merge_pdfs(pdf_list, merge_pdf_directory, merge_pdf_file_name)
        print(f"PDFs merged and saved to {os.path.join(merge_pdf_directory, merge_pdf_file_name)}")

        if merge_pdf_to_text_bool:
            pdf_to_text(os.path.join(merge_pdf_directory, merge_pdf_file_name), merge_text_directory, merge_text_file_name)
            print(f"PDFs scraped to text and saved to {os.path.join(merge_text_directory, merge_text_file_name)}")

if __name__ == '__main__':
    main()
