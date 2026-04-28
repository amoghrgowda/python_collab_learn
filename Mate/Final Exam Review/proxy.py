import os
import time
from abc import ABC, abstractmethod


class TaskAttachment(ABC):
    """Interface of a task's attachments, e.g., a PDF file, in a TODO list"""
    @abstractmethod
    def get_content(self):
        pass
    
    @abstractmethod
    def get_summary(self):
        pass


class PDFAttachment(TaskAttachment):
    """Reads a PDF file attached to a TODO"""
    
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading PDF document: {filename}")
        # simulate reading a large file
        time.sleep(1.5)

        # in reality, we would read the files
        # For this tutorial, let's set a dummy value
        self.content = f"Actual content of the pdf file {filename}"
    
    def get_content(self): # type: ignore
        return self.content
    
    def get_summary(self): # type: ignore
        return  f"PDF attachment: {self.filename}"


class AttachmentProxy(TaskAttachment):
    """Proxy for the real data - only load the real subject when necessary"""
    def __init__(self, filename):
        self.filename = filename
        self._document = None # note that wish to avoid eagerly initializing PDFAttachment
            
    def _load_document_if_needed(self):
        """Lazy initialization of the real document"""
        if self._document is None:
            print(f"\nLoading document for the first time...")
            # ??? TODO
            self._document = PDFAttachment(self.filename)
    
    def get_content(self): # type: ignore
        """This will trigger the full document load"""
        self._load_document_if_needed()
        return self._document.get_content()  # type: ignore
    
    def get_summary(self): # type: ignore
        # because get_summary doesn't need the actual content, 
        # we don't have to construct the real subject
        return f"PDF attachment: {self.filename}"

attachments = [
    AttachmentProxy("report_2025.pdf"),
    AttachmentProxy("meeting_notes.pdf"),
    AttachmentProxy("budget.pdf")
]

print("\n1. Displaying summaries of all attachments (no invocation of the real attachments yet):")
for i, attachment in enumerate(attachments, 1):
    print(f"Attachment {i}: {attachment.get_summary()}")

print("\n2. Now accessing the content of the first file:")
content1 = attachments[0].get_content()

print("\n3. Getting summary of the first file again (already loaded):")
print(f"file 1 summary: {attachments[0].get_summary()}")

print("\n4. Getting content of the second file:")
content2 = attachments[1].get_content()

print("\n5. Leaving the third attachment unloaded")