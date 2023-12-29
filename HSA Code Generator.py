
class PackagePath:
    
    def __init__(self, component, driver, package):
        """ constructor that execute when an object is created """
        self._component = component 
        self._driver = driver 
        self._package = package

    @property  # accessor / getter method
    def component(self):
        return self._component

    @property  # accessor / getter method
    def driver(self):
        return self._driver

    @property  # accessor / getter method
    def packagepath(self):
        return self._package

    def __str__(self):
        """ string representation of the object """
        return "/PackagePath:%OSDisk%\HSA\{}\{}\{}".format(self._component, self._driver, self._package)

class LicensePath:
    
    def __init__(self, component, driver, license):
        """ constructor that execute when an object is created """
        self._component = component 
        self._driver = driver 
        self._license = license

    @property  # accessor / getter method
    def component(self):
        return self._component

    @property  # accessor / getter method
    def driver(self):
        return self._driver

    @property  # accessor / getter method
    def licensepath(self):
        return self._license

    def __str__(self):
        """ string representation of the object """
        return "/LicensePath:%OSDisk%\HSA\{}\{}\{}".format(self._component, self._driver, self._license)

class DependencyPath:
    
    def __init__(self, component, driver, dependency):
        """ constructor that execute when an object is created """
        self._component = component 
        self._driver = driver 
        self._dependency = dependency

    @property  # accessor / getter method
    def component(self):
        return self._component

    @property  # accessor / getter method
    def driver(self):
        return self._driver

    @property  # accessor / getter method
    def dependencypath(self):
        return self._dependency

    def __str__(self):
        """ string representation of the object """
        return "/DependencyPackagePath:%OSDisk%\HSA\{}\{}\{}".format(self._component, self._driver, self._dependency)

################ GUI ################
import pyperclip

# after importing tkinter we will call it tk
import tkinter as tk
# import themed tk package
from tkinter import ttk
from tkinter import scrolledtext

class hsaGUI_Grid:
    def __init__(self):
        self._win = tk.Tk()
        self._win.title('HSA Code Generator - by Leariza Castor Vinteres') 
        self._win.geometry('') 
        self._win.resizable(False, False)

        #create widgets
        self.create_widgets()

        # run the application infinitely, wait for event to occur
        self._win.mainloop()

    def create_widgets(self):
        #top level frame
        dataFrame = ttk.Frame(self._win)
        dataFrame.grid(column=0, row=0)

        #component Label
        component_lbl = ttk.Label(dataFrame, text="*Component Name:")
        component_lbl.grid(column=0, row=0, padx=10, pady=8, sticky='E')

        #component Entry
        self._component = tk.StringVar()
        self._component_Ety = ttk.Entry(dataFrame,
                                      width=50,
                                      textvariable=self._component)
        self._component_Ety.grid(column=1, row=0)

        #driver Label
        driver_lbl = ttk.Label(dataFrame, text="*Driver Name:")
        driver_lbl.grid(column=0, row=1, padx=10, pady=8, sticky='NE')

        #driver Entry
        self._driver = tk.StringVar()
        self._driver_Ety = ttk.Entry(dataFrame,
                                      width=50,
                                      textvariable=self._driver)
        self._driver_Ety.grid(column=1, row=1)

        #package path Label
        packagepath_lbl = ttk.Label(dataFrame, text="*Package File Name:")
        packagepath_lbl.grid(column=0, row=2, padx=10, pady=8, sticky='NE')

        #package path Entry
        self._packagepath = tk.StringVar()
        self._packagepath_Ety = ttk.Entry(dataFrame,
                                      width=50,
                                      textvariable=self._packagepath)
        self._packagepath_Ety.grid(column=1, row=2)

        #license path Label
        licensepath_lbl = ttk.Label(dataFrame, text="*License File Name:")
        licensepath_lbl.grid(column=0, row=3, padx=10, pady=8, sticky='NE')

        #license path Entry
        self._licensepath = tk.StringVar()
        self._licensepath_Ety = ttk.Entry(dataFrame,
                                      width=50,
                                      textvariable=self._licensepath)
        self._licensepath_Ety.grid(column=1, row=3)

        #required field Label
        required_lbl = ttk.Label(dataFrame, text="*Required fields")
        required_lbl.grid(column=1, row=4, padx=10, sticky='NW')

        #dependency package path Label
        dependency_lbl = ttk.Label(dataFrame, text="Dependency Package Path(s):\n\n (💡 Tip: Separate multiple files\n  with a space)")
        dependency_lbl.grid(column=0, row=5, padx=10, pady=20, sticky='NE')

        #dependency package path Entry
        self._dependency = tk.StringVar()
        self._dependency_Ety = scrolledtext.ScrolledText(dataFrame,
                                                     width=40,
                                                     height=8,
                                                     wrap=tk.WORD)
        self._dependency_Ety.grid(column=1, row=5, pady=8)

        #button frame
        buttonFrame = ttk.Frame(dataFrame)
        buttonFrame.grid(column=1, row=6, pady=4, sticky='W')

        #button "Generate Code" in button Frame
        self._generateCode_btn = ttk.Button(buttonFrame,
                                         text='Generate Code',
                                         command=self.generateCode)
        self._generateCode_btn.grid(column=0, row=0, padx=4, sticky= 'E')

        #button "Copy Code" in button Frame
        self._generateCode_btn = ttk.Button(buttonFrame,
                                         text='Copy Code',
                                         command=self.copy)
        self._generateCode_btn.grid(column=1, row=0, padx=4, sticky= 'E')

        #button "Clear" in button Frame
        self._clear_btn = ttk.Button(buttonFrame,
                                     text='Clear All',
                                     command=self.clear)
        self._clear_btn.grid(column=2, row=0, padx=4, sticky='E')
        self._clear_btn.config(state=tk.DISABLED)

        #bottom level frame
        outputFrame = ttk.Frame(self._win)
        outputFrame.grid(column=0, row=1, padx=20, pady=10, columnspan=3)

        # create mulit-line output 50 chars x 5 lines, word wrap
        self._scroll_txt = scrolledtext.ScrolledText(outputFrame,
                                                     width=65,
                                                     height=15,
                                                     wrap=tk.WORD)
        
        # place into GRID(0,0) of outputFrame
        self._scroll_txt.grid(column=0, row=0, sticky='NSWE')
        # no editing of this ScrolledText
        self._scroll_txt.config(state=tk.DISABLED)

        # indicate where the cursor should FOCUS at the start
        self._component_Ety.focus()
    
    def generateCode(self):
         # enable the scrolledText, clear it, and disable
        self._scroll_txt.config(state=tk.NORMAL)
        self._scroll_txt.delete(1.0, tk.END)
    
        try:
            #retrieve user inputs
            component = self._component.get().strip()
            driver = self._driver.get().strip()
            package = self._packagepath.get().strip()
            license = self._licensepath.get().strip()
            dependency = self._dependency_Ety.get('1.0', 'end-1c')

            if len(component) == 0:
                raise Exception("\nRequired field : Please input Component Name.\n")
            elif len(driver) == 0:
                raise Exception("\nRequired field : Please input Driver Name.\n")
            elif len(package) == 0:
                raise Exception("\nRequired field : Please input Package File Name.\n")
            elif len(license) == 0:
                raise Exception("\nRequired field : Please input License File Name.\n")
            else:
                 None

        except Exception as e:
            self._scroll_txt.insert('end', e)
            # enable the scrolledText, clear it, and disable

        else:
            v1 = PackagePath(component, driver, package)
            v2 = LicensePath(component, driver, license)
            
            #Dependency input to list
            dependency_list = dependency.split()
            
            v3 = ""

            for d in dependency_list:
                v = DependencyPath(component, driver, d)
                v3 = v3 + str(v) + " "

            """ string representation of the object """
            line = f'DISM.exe /Image:%OSDisk%\ /Add-ProvisionedAppxPackage {v1} {v2} {v3}/Region="All"'
            
            self._scroll_txt.insert('end', line.strip())
            

        finally:
            # turn OFF the mutli-line output
            self._scroll_txt.config(state=tk.DISABLED)
            # making sure the last line is visiable (can SEE)
            self._scroll_txt.see('end')
            self._component_Ety.focus()
            self._clear_btn.config(state=tk.NORMAL)

    def copy(self):
        text = self._scroll_txt.get('1.0', 'end-1c')
        pyperclip.copy(text)

    def clear(self):
        # enable the scrolledText, clear it, and disable
        self._scroll_txt.config(state=tk.NORMAL)
        self._scroll_txt.delete(1.0, tk.END)
        self._scroll_txt.config(state=tk.DISABLED)

        self._component.set("")
        self._driver.set("")
        self._packagepath.set("")
        self._licensepath.set("")
        
        self._dependency_Ety.config(state=tk.NORMAL)
        self._dependency_Ety.delete(1.0, tk.END)

        # reset the FOCUS to Component Name input, disable CLEAR button
        self._component_Ety.focus()
        self._clear_btn.config(state=tk.DISABLED)

def main():
    hsaGUI_Grid()

main()

















