import win32com.client
import os
from datetime import datetime, timedelta

def download_pdf_attachments_today(save_folder,date):
    # Create an instance of the Outlook application
    outlook = win32com.client.Dispatch("Outlook.Application")
    mapi = outlook.GetNamespace("MAPI")
    
    # Access the inbox (you can change 'Inbox' to any other folder)
    inbox = mapi.Folders("grad.graduation@siu.edu").Folders("Inbox")
    
    # Get today's date
    # today = datetime.now().date()
    # yesterday = today - timedelta(days=1)

    
    # Loop through the messages in the inbox
    for message in inbox.Items:
        try:
            # Filter emails received today
            if message.ReceivedTime.date() == date:
                # Only process emails with attachments
                if message.Attachments.Count > 0:
                    attachment = message.Attachments
                    for att in attachment:
                        # Check if the attachment is a PDF
                        if att.FileName.endswith(".pdf"):
                            # Save attachment to the specified folder
                            att.SaveASFile(os.path.join(save_folder, att.FileName))
                            print(f"Downloaded PDF attachment from email: {message.Subject}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Folder where attachments will be saved
    today = datetime.now().date()
    for i in range(3):
        date = today - timedelta(days=i)
        save_folder = r"C:\\Users\\SIU856562516\\Desktop\\scripts\\pdf-program-clearance-processor\\"+ "attachments_"+str(date)
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        download_pdf_attachments_today(save_folder,date)
