from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime


def main():
    root = Tk()
    app = window1(root)


class window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(
            self.frame,
            text="Pharmacy Management System",
            font=("ariel", 40, "bold"),
            bd=20,
        )
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.Loginframe1 = Frame(
            self.frame, width=1000, height=300, bd=20, relief="ridge"
        )
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = Frame(
            self.frame, width=1000, height=100, bd=20, relief="ridge"
        )
        self.Loginframe2.grid(row=2, column=0)

        self.Loginframe3 = Frame(
            self.frame, width=1000, height=200, bd=20, relief="ridge"
        )
        self.Loginframe3.grid(row=3, column=0, pady=2)
        #######################################################################################################################################################################
        self.lblUsername = Label(
            self.Loginframe1, text="Username", font=("ariel", 20, "bold"), bd=22
        )
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(
            self.Loginframe1,
            font=("ariel", 20, "bold"),
            bd=22,
            textvariable=self.Username,
        )
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword = Label(
            self.Loginframe1, text="Password", font=("ariel", 20, "bold"), bd=22
        )
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(
            self.Loginframe1,
            font=("ariel", 20, "bold"),
            bd=22,
            textvariable=self.Password,
            show="*",
        )
        self.txtPassword.grid(row=1, column=1, padx=85)

        ########################################################################################################################################################################
        self.btnLogin = Button(
            self.Loginframe2,
            text="Login",
            width=17,
            font=("ariel", 20, "bold"),
            command=self.Login_System,
        )
        self.btnLogin.grid(row=0, column=0)

        self.btnReset = Button(
            self.Loginframe2,
            text="Reset",
            width=17,
            font=("ariel", 20, "bold"),
            command=self.Reset,
        )
        self.btnReset.grid(row=0, column=1)

        self.btnExit = Button(
            self.Loginframe2,
            text="Exit",
            width=17,
            font=("ariel", 20, "bold"),
            command=self.iExit,
        )
        self.btnExit.grid(row=0, column=2)
        ########################################################################################################################################################################
        self.btnRegistration = Button(
            self.Loginframe3,
            text="Patients Registration System",
            state=DISABLED,
            command=self.Registration_window,
            font=("ariel", 20, "bold"),
        )
        self.btnRegistration.grid(row=0, column=0)

        self.btnHospital = Button(
            self.Loginframe3,
            text="Hospital Management System",
            state=DISABLED,
            command=self.Hospital_window,
            font=("ariel", 20, "bold"),
        )
        self.btnHospital.grid(row=0, column=1, padx=22)

    #######################################################################################################################################################################
    def Login_System(self):
        user = self.Username.get()
        pas = self.Password.get()
        if (user == str(20004)) and (pas == str(20004)):
            self.btnRegistration.config(state=NORMAL)
            self.btnHospital.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno(
                "Pharmacy Management System", "You have entered invalid login details"
            )
            self.btnRegistration.config(state=DISABLED)
            self.btnHospital.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.btnRegistration.config(state=DISABLED)
        self.btnHospital.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno(
            "Pharmacy Management System", "Confirm if you want to exit"
        )
        if self.iExit > 0:
            self.master.destroy()
            return

    #######################################################################################################################################################################
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)


########################################################################## Window 2 ####################################################################################
class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Patients Registration System")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
        #######################################################################################################################################################################
        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d %m %y"))
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = IntVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Address = StringVar()
        Telephone = StringVar()
        Postcode = StringVar()
        ref = StringVar()
        Patientfees = StringVar()
        Patientfees.set("0")
        ########################################################################################################################################################################
        def iExit():
            iExit = tkinter.messagebox.askyesno(
                "Patient Registration System", "Confirm if you want to exit"
            )
            if iExit > 0:
                master.destroy()
                return

        def iReset():
            Firstname.set("")
            Lastname.set("")
            Address.set("")
            Telephone.set("")
            Postcode.set("")
            ref.set("")
            Patientfees.set("0")
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboProve_of_ID.current(0)
            self.cboType_of_member.current(0)
            self.cboMethod_of_Payment.current(0)
            self.txtMemberDetailsFrame.delete("1.0", END)
            return

        def ref_no():
            x = random.randint(100, 999)
            randomRef = str(x)
            ref.set(randomRef)

        def Reciept():
            ref_no()
            self.txtReciept.insert(
                END,
                "\t"
                + ref.get()
                + "\t\t"
                + Firstname.get()
                + "\t\t"
                + Lastname.get()
                + "\t\t"
                + Address.get()
                + "\t\t"
                + DateofOrder.get()
                + "\t\t"
                + Telephone.get()
                + "\t\t"
                + Patientfees.get()
                + "\n",
            )

        def Patient_fees():
            if var4.get() == 1:
                self.txtPatientfees.configure(state=NORMAL)
                Item1 = float(500)
                Patientfees.set("Rs. " + str(Item1))

            elif var4.get() == 0:
                self.txtPatientfees.configure(state=DISABLED)
                Patientfees.set("0")

        #######################################################################################################################################################################
        TitleFrame = Frame(self.frame, bd=20, width=1350, padx=26, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(
            TitleFrame, text="Patient Registration  System", font=("ariel", 30, "bold")
        )
        self.lblTitle.grid()
        ########################################################################################################################################################################
        MemberDetailsFrame = LabelFrame(
            self.frame, width=1350, height=500, bd=8, pady=5, relief=RIDGE
        )
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(
            MemberDetailsFrame, width=880, height=400, bd=3, relief=RIDGE
        )
        FrameDetails.pack(side=LEFT)

        MemberName_F = LabelFrame(
            FrameDetails,
            bd=3,
            width=35,
            height=400,
            font=("ariel", 14, "bold"),
            text="Customer Name",
            relief=RIDGE,
        )
        MemberName_F.grid(row=0, column=0)

        Reciept_ButtonFrame = LabelFrame(
            MemberDetailsFrame, bd=3, width=1000, height=400, relief=RIDGE
        )
        Reciept_ButtonFrame.pack(side=RIGHT)

        #######################################################################################################################################################################
        self.lblReferenceNo = Label(
            MemberName_F, text="Reference No", font=("ariel", 12, "bold"), bd=5
        )
        self.lblReferenceNo.grid(row=0, column=0, sticky=W)
        self.txtReferenceNo = Entry(
            MemberName_F,
            font=("ariel", 12, "bold"),
            bd=5,
            textvariable=ref,
            state=DISABLED,
            insertwidth=2,
        )
        self.txtReferenceNo.grid(row=0, column=1)

        self.lblFirstname = Label(
            MemberName_F, text="Firstname", font=("ariel", 12, "bold"), bd=5
        )
        self.lblFirstname.grid(row=1, column=0, sticky=W)
        self.txtFirstname = Entry(
            MemberName_F,
            font=("ariel", 12, "bold"),
            bd=5,
            textvariable=Firstname,
            insertwidth=2,
        )
        self.txtFirstname.grid(row=1, column=1)

        self.lblLastname = Label(
            MemberName_F, text="Lastname", font=("ariel", 12, "bold"), bd=5
        )
        self.lblLastname.grid(row=2, column=0, sticky=W)
        self.txtLastname = Entry(
            MemberName_F,
            font=("ariel", 12, "bold"),
            bd=5,
            textvariable=Lastname,
            insertwidth=2,
        )
        self.txtLastname.grid(row=2, column=1)

        self.lblAddress = Label(
            MemberName_F, text="Address", font=("ariel", 12, "bold"), bd=5
        )
        self.lblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(
            MemberName_F,
            font=("ariel", 12, "bold"),
            bd=5,
            textvariable=Address,
            insertwidth=2,
        )
        self.txtAddress.grid(row=3, column=1)

        self.lblPostcode = Label(
            MemberName_F, text="Postcode", font=("ariel", 12, "bold"), bd=5
        )
        self.lblPostcode.grid(row=4, column=0, sticky=W)
        self.txtPostcode = Entry(
            MemberName_F,
            font=("ariel", 12, "bold"),
            bd=5,
            textvariable=Postcode,
            insertwidth=2,
        )
        self.txtPostcode.grid(row=4, column=1)

        self.lblTelephone = Label(
            MemberName_F, text="Telephone", font=("ariel", 12, "bold"), bd=5
        )
        self.lblTelephone.grid(row=5, column=0, sticky=W)
        self.txtTelephone = Entry(
            MemberName_F,
            font=("ariel", 12, "bold"),
            bd=5,
            textvariable=Telephone,
            insertwidth=2,
        )
        self.txtTelephone.grid(row=5, column=1)

        self.lblDate = Label(
            MemberName_F, text="Date", font=("ariel", 12, "bold"), bd=5
        )
        self.lblDate.grid(row=6, column=0, sticky=W)
        self.txtDate = Entry(
            MemberName_F,
            font=("ariel", 14, "bold"),
            bd=5,
            textvariable=DateofOrder,
            insertwidth=2,
        )
        self.txtDate.grid(row=6, column=1)
        #######################################################################################################################################################################
        self.lblProve_of_ID = Label(
            MemberName_F, text="Prove of ID", font=("ariel", 12, "bold"), bd=5
        )
        self.lblProve_of_ID.grid(row=7, column=0, sticky=W)

        self.cboProve_of_ID = ttk.Combobox(
            MemberName_F,
            font=("ariel", 12, "bold"),
            textvariable=var1,
            state="readonly",
            width=19,
        )
        self.cboProve_of_ID["value"] = (
            "",
            "Pilot License",
            "Driving License",
            "Passport",
            "Student_ID",
        )
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7, column=1)

        self.lblType_of_member = Label(
            MemberName_F, text="Type of member", font=("ariel", 12, "bold"), bd=5
        )
        self.lblType_of_member.grid(row=8, column=0, sticky=W)

        self.cboType_of_member = ttk.Combobox(
            MemberName_F,
            font=("ariel", 12, "bold"),
            textvariable=var2,
            state="readonly",
            width=19,
        )
        self.cboType_of_member["value"] = (
            "",
            "Full Member",
            "Annual Membership",
            "Pay as you go",
        )
        self.cboType_of_member.current(0)
        self.cboType_of_member.grid(row=8, column=1)

        self.lblMethod_of_Payment = Label(
            MemberName_F, text="Method of Payment", font=("ariel", 12, "bold"), bd=3
        )
        self.lblMethod_of_Payment.grid(row=9, column=0, sticky=W)

        self.cboMethod_of_Payment = ttk.Combobox(
            MemberName_F,
            font=("ariel", 12, "bold"),
            textvariable=var3,
            state="readonly",
            width=19,
        )
        self.cboMethod_of_Payment["value"] = (
            "",
            "Visa Card",
            "Debit Card",
            "Master Card",
            "Cash",
        )
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=9, column=1)
        ########################################################################################################################################################################################

        self.chkPatientfees = Checkbutton(
            MemberName_F,
            text="Patient Fees",
            variable=var4,
            onvalue=1,
            offvalue=0,
            font=("ariel", 16, "bold"),
            command=Patient_fees,
        )
        self.chkPatientfees.grid(row=10, column=0, sticky=W)

        self.txtPatientfees = Entry(
            MemberName_F,
            font=("ariel", 14, "bold"),
            bd=7,
            textvariable=Patientfees,
            insertwidth=2,
            state=DISABLED,
            justify=RIGHT,
        )
        self.txtPatientfees.grid(row=10, column=1)
        #########################################################################################################################################################################################
        self.lblLabel = Label(
            Reciept_ButtonFrame,
            font=("ariel", 10, "bold"),
            pady=10,
            text="Member Ref\t Firstname\t Surname\t Address\t\t Date Reg.\t Telephone\t Patientfees\t",
            bd=7,
        )
        self.lblLabel.grid(row=0, column=0, columnspan=4)

        self.txtReciept = Text(
            Reciept_ButtonFrame, width=112, height=22, font=("ariel", 10, "bold")
        )
        self.txtReciept.grid(row=1, column=0, columnspan=4)
        #########################################################################################################################################################################################
        self.btnExit = Button(
            Reciept_ButtonFrame,
            padx=18,
            pady=10,
            width=13,
            text="Exit",
            command=iExit,
            font=("ariel", 10, "bold"),
        )
        self.btnExit.grid(row=2, column=2)

        self.btnReset = Button(
            Reciept_ButtonFrame,
            padx=18,
            font=("ariel", 10, "bold"),
            pady=10,
            width=13,
            text="Reset",
            command=iReset,
        )
        self.btnReset.grid(row=2, column=1)

        self.btnReciept = Button(
            Reciept_ButtonFrame,
            padx=18,
            font=("ariel", 10, "bold"),
            pady=10,
            width=13,
            text="Reciept",
            command=Reciept,
        )
        self.btnReciept.grid(row=2, column=0)


###################################################################### Window 3 #################################################################################################
class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
        #######################################################################################################################################################################
        cmbNameofTablets = StringVar()
        ReferenceNo = StringVar()
        Dose = StringVar()
        NoofTablets = StringVar()
        Lot = StringVar()
        IssueDate = StringVar()
        ExpDate = StringVar()
        DailyDose = StringVar()
        PossibleSideEffects = StringVar()
        FurtherInformation = StringVar()
        StorageAdvice = StringVar()
        DrivingUsingMachines = StringVar()
        HowtoUseMedication = StringVar()
        PatientID = StringVar()
        NHSNumber = StringVar()
        PatientName = StringVar()
        DateofBirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        #######################################################################################################################################################################
        def iExit():
            iExit = tkinter.messagebox.askyesno(
                "Hospital Management System", "Confirm if you want to exit"
            )
            if iExit > 0:
                master.destroy()
                return

        def iPrescription():
            self.txtPrescription.insert(
                END, "Name of Tablets: \t\t\t\t" + cmbNameofTablets.get() + "\n"
            )
            self.txtPrescription.insert(
                END, "Reference No: \t\t\t\t" + ReferenceNo.get() + "\n"
            )
            self.txtPrescription.insert(END, "Dose: \t\t\t\t" + Dose.get() + "\n")
            self.txtPrescription.insert(
                END, "No of Tablets: \t\t\t\t" + NoofTablets.get() + "\n"
            )
            self.txtPrescription.insert(END, "Lot: \t\t\t\t" + Lot.get() + "\n")
            self.txtPrescription.insert(
                END, "Issued Date: \t\t\t\t" + IssueDate.get() + "\n"
            )
            self.txtPrescription.insert(
                END, "Expiry Date: \t\t\t\t" + ExpDate.get() + "\n"
            )
            self.txtPrescription.insert(
                END, "Daily Dose: \t\t\t\t" + DailyDose.get() + "\n"
            )
            self.txtPrescription.insert(
                END,
                "Possible Side Effects: \t\t\t\t" + PossibleSideEffects.get() + "\n",
            )
            self.txtPrescription.insert(
                END, "Further Information: \t\t\t\t" + FurtherInformation.get() + "\n"
            )
            self.txtPrescription.insert(
                END, "Storage Advice: \t\t\t\t" + StorageAdvice.get() + "\n"
            )
            self.txtPrescription.insert(
                END,
                "Driving or Using Machines: \t\t\t\t"
                + DrivingUsingMachines.get()
                + "\n",
            )
            self.txtPrescription.insert(
                END, "How to Use Medication: \t\t\t\t" + HowtoUseMedication.get() + "\n"
            )
            self.txtPrescription.insert(
                END, "Patient ID: \t\t\t\t" + PatientID.get() + "\n"
            )
            self.txtPrescription.insert(
                END, "NHS Number: \t\t\t\t" + NHSNumber.get() + "\n"
            )
            self.txtPrescription.insert(
                END, "Patient Name: \t\t\t\t" + PatientName.get() + "\n"
            )
            self.txtPrescription.insert(
                END, "Date of Birth: \t\t\t\t" + DateofBirth.get() + "\n"
            )
            self.txtPrescription.insert(
                END, "Patient Address: \t\t\t\t" + PatientAddress.get() + "\n"
            )
            return

        def iPrescriptionData():
            self.txtFrameDetails.insert(
                END,
                cmbNameofTablets.get()
                + "\t\t"
                + ReferenceNo.get()
                + "\t\t"
                + Dose.get()
                + "\t\t"
                + NoofTablets.get()
                + "\t\t"
                + Lot.get()
                + "\t\t"
                + IssueDate.get()
                + "\t\t"
                + ExpDate.get()
                + "\t\t"
                + DailyDose.get()
                + "\t\t"
                + PossibleSideEffects.get()
                + "\t\t"
                + StorageAdvice.get()
                + "\t\t"
                + FurtherInformation.get()
                + "\t\t"
                + DrivingUsingMachines.get()
                + "\t\t"
                + HowtoUseMedication.get()
                + "\t\t"
                + PatientID.get()
                + "\t\t"
                + NHSNumber.get()
                + "\t\t"
                + PatientName.get()
                + "\t\t"
                + DateofBirth.get()
                + "\t\t"
                + PatientAddress.get()
                + "\n",
            )

        def save_iPrescriptionData(self):
            op = messagebox.askyesno(
                "Save iPrescriptionData",
                "Conform if you want to save the iPrescriptionData?",
            )
            if op == 1:
                try:
                    self.iPrescriptionData_data = self.txtarea.get()
                    f1 = open("/" + str(self.iPrescriptionData.get()) + ".txt", "w")
                    f1.write(self.iPrescriptionData_data)
                    f1.close()
                except TypeError:
                    messagebox.showerror("error", "data not saved")
            else:
                return

        def iDelete():
            cmbNameofTablets.set("")
            self.cboNameofTablets.current(0)
            ReferenceNo.set("")
            Dose.set("")
            NoofTablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            NHSNumber.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0", END)
            self.txtFrameDetails.delete("1.0", END)

            return

        def iReset():
            cmbNameofTablets.set("")
            self.cboNameofTablets.set(0)
            ReferenceNo.set("")
            Dose.set("")
            NoofTablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            NHSNumber.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0", END)

            return

        ####################################################################################################################################################################
        TitleFrame = Frame(self.frame, bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(
            TitleFrame,
            text="\tHospital Management  System\t",
            font=("ariel", 30, "bold"),
            width=39,
            padx=8,
        )
        self.lblTitle.grid()

        FrameDetails = Frame(
            self.frame, width=1350, height=100, bd=20, padx=20, relief=RIDGE
        )
        FrameDetails.pack(side=BOTTOM)

        ButtonFrame = Frame(
            self.frame, width=1350, height=50, bd=20, padx=20, relief=RIDGE
        )
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(
            self.frame, width=1350, height=400, bd=20, padx=20, relief=RIDGE
        )
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(
            DataFrame,
            width=800,
            height=300,
            bd=10,
            padx=20,
            font=("ariel", 12, "bold"),
            text="Patient Information",
            relief=RIDGE,
        )
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(
            DataFrame,
            width=450,
            height=300,
            bd=10,
            padx=20,
            font=("ariel", 12, "bold"),
            text="Prescription",
            relief=RIDGE,
        )
        DataFrameRIGHT.pack(side=RIGHT)
        ######################################################################################################################################################################
        self.lblNameofTablets = Label(
            DataFrameLEFT,
            text="Name of Tablet",
            font=("ariel", 12, "bold"),
            padx=2,
            pady=2,
        )
        self.lblNameofTablets.grid(row=0, column=0, sticky=W)

        self.cboNameofTablets = ttk.Combobox(
            DataFrameLEFT,
            font=("ariel", 14, "bold"),
            textvariable=cmbNameofTablets,
            state="readonly",
            width=23,
        )
        self.cboNameofTablets["value"] = (
            "",
            "Crocin",
            "Streptomising",
            "Zydip-C",
            "Disprin",
        )
        self.cboNameofTablets.current(0)
        self.cboNameofTablets.grid(row=0, column=1)

        self.lblFurtherInformation = Label(
            DataFrameLEFT,
            text="Further Information",
            font=("ariel", 12, "bold"),
            padx=2,
            pady=2,
        )
        self.lblFurtherInformation.grid(row=0, column=2, sticky=W)
        self.txtFurtherInformation = Entry(
            DataFrameLEFT,
            font=("ariel", 12, "bold"),
            textvariable=FurtherInformation,
            width=25,
        )
        self.txtFurtherInformation.grid(row=0, column=3)

        self.lblReferenceNo = Label(
            DataFrameLEFT,
            text="Reference No",
            font=("ariel", 12, "bold"),
            padx=2,
            pady=2,
        )
        self.lblReferenceNo.grid(row=1, column=0, sticky=W)
        self.txtReferenceNo = Entry(
            DataFrameLEFT,
            font=("ariel", 12, "bold"),
            textvariable=ReferenceNo,
            width=25,
        )
        self.txtReferenceNo.grid(row=1, column=1)

        self.lblStorageAdvice = Label(
            DataFrameLEFT,
            text="Storage Advice",
            font=("ariel", 12, "bold"),
            padx=2,
            pady=2,
        )
        self.lblStorageAdvice.grid(row=1, column=2, sticky=W)
        self.txtStorageAdvice = Entry(
            DataFrameLEFT,
            font=("ariel", 12, "bold"),
            textvariable=StorageAdvice,
            width=25,
        )
        self.txtStorageAdvice.grid(row=1, column=3)

        self.lblDose = Label(
            DataFrameLEFT, text="Dose", font=("ariel", 12, "bold"), padx=2, pady=2
        )
        self.lblDose.grid(row=2, column=0, sticky=W)
        self.txtDose = Entry(
            DataFrameLEFT, font=("ariel", 12, "bold"), textvariable=Dose, width=25
        )
        self.txtDose.grid(row=2, column=1)

        self.lblDrivingUsingMachines = Label(
            DataFrameLEFT,
            text="Driving or Using Machines",
            font=("ariel", 12, "bold"),
            padx=2,
            pady=2,
        )
        self.lblDrivingUsingMachines.grid(row=2, column=2, sticky=W)
        self.txtDrivingUsingMachines = Entry(
            DataFrameLEFT,
            font=("ariel", 12, "bold"),
            textvariable=DrivingUsingMachines,
            width=25,
        )
        self.txtDrivingUsingMachines.grid(row=2, column=3)

        self.lblNoofTablets = Label(
            DataFrameLEFT,
            text="No of Tablets",
            font=("ariel", 12, "bold"),
            padx=2,
            pady=2,
        )
        self.lblNoofTablets.grid(row=3, column=0, sticky=W)
        self.txtNoofTablets = Entry(
            DataFrameLEFT,
            font=("ariel", 12, "bold"),
            textvariable=NoofTablets,
            width=25,
        )
        self.txtNoofTablets.grid(row=3, column=1)

        self.lblHowtoUseMedication = Label(
            DataFrameLEFT,
            text="How t oUse Medication",
            font=("ariel", 12, "bold"),
            padx=2,
            pady=2,
        )
        self.lblHowtoUseMedication.grid(row=3, column=2, sticky=W)
        self.txtHowtoUseMedication = Entry(
            DataFrameLEFT,
            font=("ariel", 12, "bold"),
            textvariable=HowtoUseMedication,
            width=25,
        )
        self.txtHowtoUseMedication.grid(row=3, column=3)

        self.lblLot = Label(
            DataFrameLEFT, text="Lot", font=("ariel", 12, "bold"), padx=2, pady=2
        )
        self.lblLot.grid(row=4, column=0, sticky=W)
        self.txtLot = Entry(
            DataFrameLEFT, font=("ariel", 12, "bold"), textvariable=Lot, width=25
        )
        self.txtLot.grid(row=4, column=1)

        self.lblPatientID = Label(
            DataFrameLEFT, text="Patient ID", font=("ariel", 12, "bold"), padx=2, pady=2
        )
        self.lblPatientID.grid(row=4, column=2, sticky=W)
        self.txtPatientID = Entry(
            DataFrameLEFT, font=("ariel", 12, "bold"), textvariable=PatientID, width=25
        )
        self.txtPatientID.grid(row=4, column=3)

        self.lblIssueDate = Label(
            DataFrameLEFT,
            text="Issued Date",
            font=("ariel", 12, "bold"),
            padx=2,
            pady=2,
        )
        self.lblIssueDate.grid(row=5, column=0, sticky=W)
        self.txtIssueDate = Entry(
            DataFrameLEFT, font=("ariel", 12, "bold"), textvariable=IssueDate, width=25
        )
        self.txtIssueDate.grid(row=5, column=1)

        self.lblNHSNumber = Label(
            DataFrameLEFT, text="NHS Number", font=("ariel", 12, "bold"), padx=2, pady=2
        )
        self.lblNHSNumber.grid(row=5, column=2, sticky=W)
        self.txtNHSNumber = Entry(
            DataFrameLEFT, font=("ariel", 12, "bold"), textvariable=NHSNumber, width=25
        )
        self.txtNHSNumber.grid(row=5, column=3)

        self.lblExpDate = Label(
            DataFrameLEFT,
            text="Expiry Date",
            font=("ariel", 12, "bold"),
            padx=2,
            pady=2,
        )
        self.lblExpDate.grid(row=6, column=0, sticky=W)
        self.txtExpDate = Entry(
            DataFrameLEFT, font=("ariel", 12, "bold"), textvariable=ExpDate, width=25
        )
        self.txtExpDate.grid(row=6, column=1)

        self.lblPatientName = Label(
            DataFrameLEFT,
            text="Patient Name",
            font=("ariel", 12, "bold"),
            padx=2,
            pady=2,
        )
        self.lblPatientName.grid(row=6, column=2, sticky=W)
        self.txtPatientName = Entry(
            DataFrameLEFT,
            font=("ariel", 12, "bold"),
            textvariable=PatientName,
            width=25,
        )
        self.txtPatientName.grid(row=6, column=3)

        self.lblDailyDose = Label(
            DataFrameLEFT, text="Daily Dose", font=("ariel", 12, "bold"), padx=2, pady=2
        )
        self.lblDailyDose.grid(row=7, column=0, sticky=W)
        self.txtDailyDose = Entry(
            DataFrameLEFT, font=("ariel", 12, "bold"), textvariable=DailyDose, width=25
        )
        self.txtDailyDose.grid(row=7, column=1)

        self.lblDateofBirth = Label(
            DataFrameLEFT,
            text="Date of Birth",
            font=("ariel", 12, "bold"),
            padx=2,
            pady=2,
        )
        self.lblDateofBirth.grid(row=7, column=2, sticky=W)
        self.txtDateofBirth = Entry(
            DataFrameLEFT,
            font=("ariel", 12, "bold"),
            textvariable=DateofBirth,
            width=25,
        )
        self.txtDateofBirth.grid(row=7, column=3)

        self.lblPossibleSideEffects = Label(
            DataFrameLEFT,
            text="Possible Side Effects",
            font=("ariel", 12, "bold"),
            padx=2,
            pady=2,
        )
        self.lblPossibleSideEffects.grid(row=8, column=0, sticky=W)
        self.txtPossibleSideEffects = Entry(
            DataFrameLEFT,
            font=("ariel", 12, "bold"),
            textvariable=PossibleSideEffects,
            width=25,
        )
        self.txtPossibleSideEffects.grid(row=8, column=1)

        self.lblPatientAddress = Label(
            DataFrameLEFT,
            text="Patient Address",
            font=("ariel", 12, "bold"),
            padx=2,
            pady=2,
        )
        self.lblPatientAddress.grid(row=8, column=2, sticky=W)
        self.txtPatientAddress = Entry(
            DataFrameLEFT,
            font=("ariel", 12, "bold"),
            textvariable=PatientAddress,
            width=25,
        )
        self.txtPatientAddress.grid(row=8, column=3)
        ####################################################################################################################################################################
        self.txtPrescription = Label(
            DataFrameRIGHT,
            font=("ariel", 12, "bold"),
            padx=2,
            pady=6,
            width=43,
            height=12,
        )
        self.txtPrescription.grid(row=0, column=0)
        ###################################################################################################################################################################
        self.btnPrescription = Button(
            ButtonFrame,
            text="Prescription",
            font=("ariel", 12, "bold"),
            width=24,
            bd=4,
            command=iPrescription,
        )
        self.btnPrescription.grid(row=0, column=0)

        self.btnPrescriptionData = Button(
            ButtonFrame,
            text="Prescription Data",
            font=("ariel", 12, "bold"),
            width=24,
            bd=4,
            command=iPrescriptionData,
        )
        self.btnPrescriptionData.grid(row=0, column=1)

        self.btnDelete = Button(
            ButtonFrame,
            text="Delete",
            font=("ariel", 12, "bold"),
            width=24,
            bd=4,
            command=iDelete,
        )
        self.btnDelete.grid(row=0, column=2)

        self.btnReset = Button(
            ButtonFrame,
            text="Reset",
            font=("ariel", 12, "bold"),
            width=24,
            bd=4,
            command=iReset,
        )
        self.btnReset.grid(row=0, column=3)

        self.btnExit = Button(
            ButtonFrame,
            text="Exit",
            font=("ariel", 12, "bold"),
            width=24,
            bd=4,
            command=iExit,
        )
        self.btnExit.grid(row=0, column=4)
        #######################################################################################################################################################################
        self.lblLabel = Label(
            FrameDetails,
            font=("ariel", 8, "bold"),
            pady=8,
            text="Name of Tablets\tReference No\t Dosage \tNo of Tablets\t Lot \t Issued Date\t Exp Date\t Daily Dose\t Storage Adv. \tNHS Number\t Patient Name\t DOB\t Address",
        )
        self.lblLabel.grid(row=0, column=0)

        self.txtFrameDetails = Text(
            FrameDetails, font=("ariel", 8, "bold"), width=200, height=4, padx=2, pady=4
        )
        self.txtFrameDetails.grid(row=1, column=0)


####################################################################################################################################################################
if __name__ == "__main__":
    main()

