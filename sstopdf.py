import pyautogui #importeert de package
from PIL import Image #van PIL import het image

myScreenshot = pyautogui.screenshot() #verkorting van pyautogoi.screenshot()
screenshotPath = r'ss.png' #waar de screenshot wordt opgeslagen. in dit geval in dezelfde folder.
myScreenshot.save(screenshotPath) #slaat de screenshot op in de screenshotpath

image1 = Image.open(screenshotPath) #opent de screenshot die je zojuist hebt gemaakt
im1 = image1.convert('RGB') #word geconvert naar pdf
pdfPath = r'new-ss.pdf' #waar de screenshot wordt opgeslagen. in dit geval in dezelfde folder.
im1.save(pdfPath) #word opgeslagen