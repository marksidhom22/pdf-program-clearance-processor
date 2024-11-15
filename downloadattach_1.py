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
    i=0
    for message in inbox.Items:
        try:
            # Filter emails received today
            # message.ReceivedTime.date() == date and
            if  "Mark_PC_Form" in message.Categories and "Mark_PCForm_Downloaded" not in  message.Categories:
                # Only process emails with attachments
                if message.Attachments.Count > 0:
                    attachment = message.Attachments
                    for att in attachment:
                        # Check if the attachment is a PDF
                        if att.FileName.endswith(".pdf"):
                            # Save attachment to the specified folder
                            att.SaveASFile(os.path.join(save_folder, str(i)+att.FileName))
                            i+=1
                            
                            # Preserve existing categories and add "Mark_PCForm_Downloaded"
                            existing_categories = message.Categories
                            new_categories = f"{existing_categories}, Mark_PCForm_Downloaded" if existing_categories else "Mark_PCForm_Downloaded"
                            message.Categories = new_categories
                            message.Save()  # Save changes to the message in Outlook
                            print(f"Email category set to '{new_categories}' for email: {message.Subject}")


                            print(f"Downloaded PDF attachment from sender: {message.SenderName}")
        except Exception as e:
             print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Folder where attachments will be saved
    today = datetime.now().date()
    for i in range(3):
        date = today - timedelta(days=i)
        save_folder = r"C:/Users/marks/Downloads/pdf-program-clearance-processor/attachments_"+str(date)
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        download_pdf_attachments_today(save_folder,date)
