# pdf-merge-and-scrape

Author:  James Bullock

This repository provides a Python script to find PDF files in a directory, merge them into a single document, and scrape the text from the merged document. We use the PyPDF2 library to work with PDF files.

Functions:

find_pdfs(directory): Finds all PDF files in a given directory and returns a list of file paths for all PDF files in the directory.

merge_pdfs(pdf_file_list, target_directory, master_file_name): Merges a list of PDF files into a single PDF and saves it to the specified directory.

pdf_to_text(pdf_file_path, target_directory, txt_file_name): Converts a PDF file to a text file and saves it to the specified directory.

main(): The main function that calls the other functions to find, merge, and convert PDF files.

The main() function accepts the following arguments:

find_pdfs_directory: The directory to search for PDF files. Default is the current working directory.
merge_pdf_directory: The directory to save the merged PDF to. Default is the current working directory.
merge_pdf_file_name: The name to use for the merged PDF file. Default is 'Merged_PDFs.pdf'.
merge_text_directory: The directory to save the text file to. Default is the current working directory.
merge_text_file_name: The name to use for the text file. Default is 'Scraped_PDFs_to_Text.txt'.
merge_pdfs_bool: Whether or not to merge the PDF files. Default is True. If set to False, the PDF files will not be merged.
merge_pdf_to_text_bool: Whether or not to convert the merged PDF to text. Default is True. If set to False, the merged PDF will not be converted to text.

