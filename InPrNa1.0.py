#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
# pymol lib
try:
    from pymol import cmd
    from pymol import *
    #from cgo import *
except ImportError:
    print 'Warning: pymol library cmd not found.'
    sys.exit(1)

# external lib
try:
    import Pmw
except ImportError:
    print 'Warning: failed to import Pmw. Exit ...'
    sys.exit(1)


try:
    import ttk
    import tkFileDialog
    import tkColorChooser
except ImportError:
    print 'Warning: failed to import ttk or tk. Exit ...'
try:
    import numpy
except ImportError:
    print 'Warning: failed to import numpy. Exit ...'

try:
    import math
except ImportError:
    print 'Warning: failed to import math. Exit ...'
try:
    import Tkinter
    from Tkinter import *


except:
    import tkinter
    import _tkinter
#from Tkinter import ScrolledText
try:
    import ScrolledText as tkst

except:
    import tkinter.scrolledtext as tkst
    print 'Warning: failed to import ScrolledText. Exit ...'


def __init__(self):
    self.menuBar.addmenuitem('Plugin', 'command',
                             'Interface Show', label='InPrNa1.0',
                             command=lambda s=self: start(s))


class start:
    def __init__(self, app):
        self.counter = 0.0
        ##interface information
        self.pdbfile = ''
        self.Resn_number = {'ALA': 0,
                            'ARG': 0,
                            'ASN': 0,
                            'ASP': 0,
                            'CYS': 0,
                            'GLN': 0,
                            'GLU': 0,
                            'GLY': 0,
                            'HIS': 0,
                            'ILE': 0,
                            'LEU': 0,
                            'LYS': 0,
                            'MET': 0,
                            'PHE': 0,
                            'PRO': 0,
                            'SER': 0,
                            'THR': 0,
                            'TRP': 0,
                            'TYR': 0,
                            'VAL': 0,
                            }


        self.interface3_resn_number = {'ALA': 0,
                            'ARG': 0,
                            'ASN': 0,
                            'ASP': 0,
                            'CYS': 0,
                            'GLN': 0,
                            'GLU': 0,
                            'GLY': 0,
                            'HIS': 0,
                            'ILE': 0,
                            'LEU': 0,
                            'LYS': 0,
                            'MET': 0,
                            'PHE': 0,
                            'PRO': 0,
                            'SER': 0,
                            'THR': 0,
                            'TRP': 0,
                            'TYR': 0,
                            'VAL': 0,
                            }
        self.interface35_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface4_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface45_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface5_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface55_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface6_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface65_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface7_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface75_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface8_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface85_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface9_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface95_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface10_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }




        #interface pdb infotmation
        self.interface3_lead = []
        self.interface35_lead = []
        self.interface4_lead = []
        self.interface45_lead = []
        self.interface5_lead = []
        self.interface55_lead = []
        self.interface6_lead = []
        self.interface65_lead = []
        self.interface7_lead = []
        self.interface75_lead = []
        self.interface8_lead = []
        self.interface85_lead = []
        self.interface9_lead = []
        self.interface95_lead = []
        self.interface10_lead = []



        ##############
        self.DNA_atom = []
        self.protein_atom = []
##############################################
        self.bump_Classify_6 = {'valley':[],
                              'flat':[],
                              'peak':[]}


##############################################

        self.INTERFACE_DIS_3 = []
        self.INTERFACE_DIS_35 = []
        self.INTERFACE_DIS_4 = []
        self.INTERFACE_DIS_45 = []
        self.INTERFACE_DIS_5 = []
        self.INTERFACE_DIS_55 = []
        self.INTERFACE_DIS_6 = []
        self.INTERFACE_DIS_65 = []
        self.INTERFACE_DIS_7 = []
        self.INTERFACE_DIS_75 = []
        self.INTERFACE_DIS_8 = []
        self.INTERFACE_DIS_85 = []
        self.INTERFACE_DIS_9 = []
        self.INTERFACE_DIS_95 = []
        self.INTERFACE_DIS_10 = []

        self.app1 = app
        self.parent = app.root
        self.dialog = Pmw.Dialog(self.parent,
                                 buttons=('Browse', 'load PDB', 'Cancel'),
                                 command=self.Ask_Dialog_Cmd)

        # pdb_load_Ent = Entry(self.dialog.interior(), textvariable=self.pdb_file_path, width=35)
        self.pdb_load_Ent = Text(self.dialog.interior(),height=1, width=30)
        # pdb_load_Ent.delete()
        self.pdb_load_Ent.grid(sticky='E')

    def Ask_Dialog_Cmd(self, cmd ):
        if cmd == 'Browse':
            self.GetPDBFilePath()
            # self.pdb_file_path.set(self.pdbfile)
            self.pdb_load_Ent.delete(1.0,Tkinter.END)
            self.pdb_load_Ent.insert(END,self.pdbfile)


        elif cmd == 'load PDB':
            # print 'hello'
            self.LoadPDB(self.pdbfile)
            self.dialog.withdraw()
            self.plugin = Plugin(self.app1, self.pdbfile)


            self.plugin.Resn_number = self.Resn_number
            self.plugin.interface6_resn_number = self.interface6_resn_number

            self.plugin.interface3_resn_number = self.interface3_resn_number
            self.plugin.interface35_resn_number = self.interface35_resn_number
            self.plugin.interface4_resn_number = self.interface4_resn_number
            self.plugin.interface45_resn_number = self.interface45_resn_number
            self.plugin.interface5_resn_number = self.interface5_resn_number
            self.plugin.interface55_resn_number = self.interface55_resn_number
            self.plugin.interface6_resn_number = self.interface6_resn_number
            self.plugin.interface65_resn_number = self.interface65_resn_number
            self.plugin.interface7_resn_number = self.interface7_resn_number
            self.plugin.interface75_resn_number = self.interface75_resn_number
            self.plugin.interface8_resn_number = self.interface8_resn_number
            self.plugin.interface85_resn_number = self.interface85_resn_number
            self.plugin.interface9_resn_number = self.interface9_resn_number
            self.plugin.interface95_resn_number = self.interface95_resn_number
            self.plugin.interface10_resn_number = self.interface10_resn_number




            self.plugin.bump_Classify_6 = self.bump_Classify_6
            self.plugin.bump_Classify_3 = self.bump_Classify_3
            self.plugin.bump_Classify_35 = self.bump_Classify_35
            self.plugin.bump_Classify_4 = self.bump_Classify_4
            self.plugin.bump_Classify_45 = self.bump_Classify_45
            self.plugin.bump_Classify_all = self.bump_Classify_all

            self.plugin.bump_Classify_set["all_protein"] = self.bump_Classify_all
            self.plugin.bump_Classify_set["3angstrom"] = self.bump_Classify_3
            self.plugin.bump_Classify_set["3.5angstrom"] = self.bump_Classify_35
            self.plugin.bump_Classify_set["4angstrom"] = self.bump_Classify_4
            self.plugin.bump_Classify_set["4.5angstrom"] = self.bump_Classify_45
            self.plugin.bump_Classify_set["6angstrom"] = self.bump_Classify_6

            self.plugin.interface3_lead = self.interface3_lead
            self.plugin.interface35_lead = self.interface35_lead
            self.plugin.interface4_lead = self.interface4_lead
            self.plugin.interface45_lead = self.interface45_lead
            self.plugin.interface5_lead = self.interface5_lead
            self.plugin.interface55_lead = self.interface55_lead
            self.plugin.interface6_lead = self.interface6_lead
            self.plugin.interface65_lead = self.interface65_lead
            self.plugin.interface7_lead = self.interface7_lead
            self.plugin.interface75_lead = self.interface75_lead
            self.plugin.interface8_lead = self.interface8_lead
            self.plugin.interface85_lead = self.interface85_lead
            self.plugin.interface9_lead = self.interface9_lead
            self.plugin.interface95_lead = self.interface95_lead
            self.plugin.interface10_lead = self.interface10_lead


            # print "flat"

            self.plugin.bump_Classify_flat=self.bump_Classify_all
            self.plugin.bump_Classify_peak=self.bump_Classify_all
            self.plugin.bump_Classify_valley=self.bump_Classify_all

            self.plugin.INTERFACE_DIS_3 = self.INTERFACE_DIS_3
            self.plugin.INTERFACE_DIS_35 = self.INTERFACE_DIS_35
            self.plugin.INTERFACE_DIS_4 = self.INTERFACE_DIS_4
            self.plugin.INTERFACE_DIS_45 = self.INTERFACE_DIS_45
            self.plugin.INTERFACE_DIS_5 = self.INTERFACE_DIS_5
            self.plugin.INTERFACE_DIS_55 = self.INTERFACE_DIS_55
            self.plugin.INTERFACE_DIS_6 = self.INTERFACE_DIS_6
            self.plugin.INTERFACE_DIS_65 = self.INTERFACE_DIS_65
            self.plugin.INTERFACE_DIS_7 = self.INTERFACE_DIS_7
            self.plugin.INTERFACE_DIS_75 = self.INTERFACE_DIS_75
            self.plugin.INTERFACE_DIS_8 = self.INTERFACE_DIS_8
            self.plugin.INTERFACE_DIS_85 = self.INTERFACE_DIS_85
            self.plugin.INTERFACE_DIS_9 = self.INTERFACE_DIS_9
            self.plugin.INTERFACE_DIS_95 = self.INTERFACE_DIS_95
            self.plugin.INTERFACE_DIS_10 = self.INTERFACE_DIS_10


            self.plugin.INTERFACE_CONTENT = self.INTERFACE_DIS_6


        elif cmd == 'Cancel':
            print('Exiting Plugin ...')
            if __name__ == '__main__':
                self.parent.destroy()
            else:
                self.dialog.withdraw()
            print('Done.')
        else:
            self.dialog.withdraw()

    def GetPDBFilePath(self):
        self.pdbfile = tkFileDialog.askopenfilename()

    def LoadPDB(self, pdbfile):
        if pdbfile is not None:
            cmd.load(pdbfile)
            cmd.color('gray')
            cmd.show('sphere')
            ############
            ## Main
            ###########
            atom_content_dir = self.Open_PDB_content(pdbfile)
            self.All_protein_Atom = self.calcu_durg_pdb_interface(pdbfile)

            self.bump_Classify_all = self.BumpClassify(self.protein_atom,atom_content_dir)
            self.bump_Classify_6 = self.BumpClassify(self.INTERFACE_DIS_6, atom_content_dir)
            self.bump_Classify_3 = self.BumpClassify(self.INTERFACE_DIS_3, atom_content_dir)
            self.bump_Classify_35 = self.BumpClassify(self.INTERFACE_DIS_35, atom_content_dir)
            self.bump_Classify_4 = self.BumpClassify(self.INTERFACE_DIS_4, atom_content_dir)
            self.bump_Classify_45 = self.BumpClassify(self.INTERFACE_DIS_45, atom_content_dir)
            self.progress_window.destroy()



            #SELECT INTERFACE



            cmd.select('nucleic', 'resn DA+DC+DG+DT+DU+A+T+G+C+I+U+5IU')

            # cmd.select("interface", resn + ' and ' + resi + ' and ' + chain,)
            self.selector(self.INTERFACE_DIS_6,"interface")
            cmd.create("INTERFACE1", "interface")
            # cmd.hide()

            self.selector(self.All_protein_Atom,"protein")
            # cmd.hide("everything", "protein")
            # cmd.show("surface","protein")
            # cmd.create("PROTEIN", "protein")
            # cmd.hide("everything", "protein")

            cmd.select('nucleic', 'resn DA+DC+DG+DT+DU+A+T+G+C+I+U+5IU')
            #cmd.extract("protein","proteins")
            #cmd.extract("Nucleic","Nucleics")


        else:
            print ('NO Path Input')

    def calcu_dis(self, coord_1, coord_2):

        coord_1_X = float(coord_1[0])
        coord_1_Y = float(coord_1[1])
        coord_1_Z = float(coord_1[2])
        coord_2_X = float(coord_2[0])
        coord_2_Y = float(coord_2[1])
        coord_2_Z = float(coord_2[2])

        Euclid_Dis = math.sqrt(
            ((coord_1_X - coord_2_X) ** 2) + ((coord_1_Y - coord_2_Y) ** 2) + ((coord_1_Z - coord_2_Z) ** 2))

        return Euclid_Dis


    #no DNA
    def Open_PDB_content(self, pdb_file_name):
        file_handle = open(pdb_file_name, 'r')
        counter = 0
        atom_content_dir = {}
        for file_content in file_handle:
            if file_content[0:4] == 'ATOM':
                if file_content[17:20] != ' DA' and \
                                file_content[17:20] != ' DT' and \
                                file_content[17:20] != ' DG' and \
                                file_content[17:20] != ' DC' and \
                                file_content[17:20] != '  A' and \
                                file_content[17:20] != '  C' and \
                                file_content[17:20] != '  G' and \
                                file_content[17:20] != '  T' and \
                                file_content[17:20] != '  U' and \
                                file_content[17:20] != '  I':
                    atom_content_dir[counter] = file_content
                    counter = counter + 1
        # print counter

        return atom_content_dir

    def Calcu_PDB_CA_SI(self, Valid_ATOM_Num):

        Vint = Valid_ATOM_Num * 20.1
        Vsphere = 4 * math.pi * 12 ** 3 / 3
        Vext = Vsphere - Vint
        CX = (Vext - Vint) / Vsphere
        return CX

    def calcu_durg_pdb_interface(self, pdb_file_name):

        ATOM_content = []
        DX_content = []

        pdb_content_handle = open(pdb_file_name, 'r')
        for DX_Cell in pdb_content_handle:
            if DX_Cell[0:4] == 'ATOM':
                self.counter += 1
                if DX_Cell[17:20] == ' DA' or \
                                DX_Cell[17:20] == ' DT' or \
                                DX_Cell[17:20] == ' DG' or \
                                DX_Cell[17:20] == ' DC' or \
                                DX_Cell[17:20] == '  A' or \
                                DX_Cell[17:20] == '  C' or \
                                DX_Cell[17:20] == '  G' or \
                                DX_Cell[17:20] == '  T' or \
                                DX_Cell[17:20] == '  U' or \
                                DX_Cell[17:20] == '  I' :
                                # and DX_Cell[13:15] == 'CA':
                    # print DX_Cell
                    DX_content.append(DX_Cell)
                else:
                    if DX_Cell[13:15] == 'CA':
                        self.Resn_number[DX_Cell[17:20]] += 1
                    ATOM_content.append(DX_Cell)
        pdb_content_handle.close()

        self.protein_atom = ATOM_content
        self.DNA_atom = DX_content



#   progress tk window

        self.progress_window = Tk()


        self.progress_window.title('Calculating')
        self.progress_window.geometry('630x150')

        ## 设置进度条
        ttk.Label(self.progress_window, text='Progress:', ).place(x=45, y=60)
        self.canvas = Canvas(self.progress_window, width=465, height=22, bg="white")
        self.fill_line = self.canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
        self.canvas.place(x=110, y=60)



        x = self.counter  # 未知变量，可更改
        self.progress_counters = float(465.0/self.counter)  # 是矩形填充满的次数
        # print  n

##################################

        for Atom in ATOM_content:
            min_dis = 9999
            Atom_cood = [Atom[30:38], Atom[38:46], Atom[46:54]]
            interface_flag = 0
            ####progress
            self.progress_counters = float(self.progress_counters + 465.0 / x)
            info_6 = ""
            for Dx in DX_content:
                DX_cood = [Dx[30:38], Dx[38:46], Dx[46:54]]
                dis = self.calcu_dis(Atom_cood, DX_cood)
                info = Atom[:26] + " --- " + Dx[:26]
                if min_dis > dis:
                    min_dis = dis
                    info_6 = Atom[:26] + " --- " + Dx[:26]

            if min_dis < 6:
                self.INTERFACE_DIS_6.append(Atom)
                self.interface6_lead.append(info_6)
                if Atom[13:15] == 'CA':
                    self.interface6_resn_number[Atom[17:20]] += 1
            if min_dis < 3:
                self.INTERFACE_DIS_3.append(Atom)
                self.interface3_lead.append(info_6)
                if Atom[13:15] == 'CA':
                  self.interface3_resn_number[Atom[17:20]] += 1
            if min_dis < 3.5:
                self.INTERFACE_DIS_35.append(Atom)
                self.interface35_lead.append(info_6)
                if Atom[13:15] == 'CA':
                  self.interface35_resn_number[Atom[17:20]] += 1
            if min_dis < 4:
                self.INTERFACE_DIS_4.append(Atom)
                self.interface4_lead.append(info_6)
                if Atom[13:15] == 'CA':
                  self.interface4_resn_number[Atom[17:20]] += 1
            if min_dis < 4.5:
                self.INTERFACE_DIS_45.append(Atom)
                self.interface45_lead.append(info_6)
                if Atom[13:15] == 'CA':
                  self.interface45_resn_number[Atom[17:20]] += 1
            if min_dis < 5.5:
                self.INTERFACE_DIS_55.append(Atom)
                self.interface55_lead.append(info_6)
                if Atom[13:15] == 'CA':
                  self.interface55_resn_number[Atom[17:20]] += 1
            if min_dis < 6.5:
                self.INTERFACE_DIS_65.append(Atom)
                self.interface65_lead.append(info_6)
                if Atom[13:15] == 'CA':
                  self.interface65_resn_number[Atom[17:20]] += 1
            if min_dis < 7:
                self.INTERFACE_DIS_7.append(Atom)
                self.interface7_lead.append(info_6)
                if Atom[13:15] == 'CA':
                  self.interface7_resn_number[Atom[17:20]] += 1
            if min_dis < 7.5:
                self.INTERFACE_DIS_75.append(Atom)
                self.interface75_lead.append(info_6)
                if Atom[13:15] == 'CA':
                  self.interface75_resn_number[Atom[17:20]] += 1
            if min_dis < 8:
                self.INTERFACE_DIS_8.append(Atom)
                self.interface8_lead.append(info_6)
                if Atom[13:15] == 'CA':
                  self.interface8_resn_number[Atom[17:20]] += 1
            if min_dis < 8.5:
                self.INTERFACE_DIS_85.append(Atom)
                self.interface85_lead.append(info_6)
                if Atom[13:15] == 'CA':
                  self.interface85_resn_number[Atom[17:20]] += 1
            if min_dis < 9:
                self.INTERFACE_DIS_9.append(Atom)
                self.interface9_lead.append(info_6)
                if Atom[13:15] == 'CA':
                  self.interface9_resn_number[Atom[17:20]] += 1
            if min_dis < 9.5:
                self.INTERFACE_DIS_95.append(Atom)
                self.interface95_lead.append(info_6)
                if Atom[13:15] == 'CA':
                  self.interface95_resn_number[Atom[17:20]] += 1
            if min_dis < 10:
                self.INTERFACE_DIS_10.append(Atom)
                self.interface10_lead.append(info_6)
                if Atom[13:15] == 'CA':
                  self.interface10_resn_number[Atom[17:20]] += 1



            self.canvas.coords(self.fill_line, (0, 0, self.progress_counters, 60))
            self.progress_window.update()

        return ATOM_content
        # print Interface_content


    def calcu_dis(self, coord_1, coord_2):

        coord_1_X = float(coord_1[0])
        coord_1_Y = float(coord_1[1])
        coord_1_Z = float(coord_1[2])
        coord_2_X = float(coord_2[0])
        coord_2_Y = float(coord_2[1])
        coord_2_Z = float(coord_2[2])

        Euclid_Dis = numpy.sqrt(
            ((coord_1_X - coord_2_X) ** 2) + ((coord_1_Y - coord_2_Y) ** 2) + ((coord_1_Z - coord_2_Z) ** 2))

        return Euclid_Dis

    def BumpClassify(self, Atom_content, atom_content_dir):

        bump_Classify = {'valley':[],
                              'flat':[],
                              'peak':[]}

        for Cell in Atom_content:
            # print Cell
            ca_cood = (Cell[30:38], Cell[38:46], Cell[46:54])
            atom_counter = 0

            for key in atom_content_dir:
                coord_2 = (atom_content_dir[key][30:38], atom_content_dir[key][38:46], atom_content_dir[key][46:54])
                dis = self.calcu_dis(ca_cood, coord_2)
                if dis < 12:
                    atom_counter = atom_counter + 1
            CX = self.Calcu_PDB_CA_SI(atom_counter)
            # print CX
            if CX < -0.2:
                shape = "valley"
                bump_Classify['valley'].append(Cell)
                # self.valleyCell.append(Cell)

            elif CX < 0.2:
                shape = 'flat'
                bump_Classify['flat'].append(Cell)
                # self.flatCell.append(Cell)

            else:
                shape = "peak"
                bump_Classify['peak'].append(Cell)
                # self.peakCell.append(Cell)
        return bump_Classify
    def selector(self,content,sele_name):
        for i in content:
            # con_list.append(i[17:20])
            cmd.select(sele_name, ' resn ' +i[17:20]+ ' and  resi' + i[22:26] + ' and chain ' +i[21],merge=1)


#################
# GUI related
#################
class Plugin:
    def __init__(self, app, pdbfile):
        self.parent = app.root
        self.pdb_file_path = pdbfile
        self.DIS = 6
        self.interface_mod = "spheres"
        self.protein_mod = "spheres"

        self.INTERFACE_CONTENT = []

        ###############################
        #dafault all_protein
        self.bump_Classify_valley = {'valley': [],
                              'flat': [],
                              'peak': []}
        self.bump_Classify_flat = {'valley': [],
                              'flat': [],
                              'peak': []}
        self.bump_Classify_peak = {'valley': [],
                              'flat': [],
                              'peak': []}
        self.bump_Classify_all={'valley': [],
                                'flat': [],
                                'peak': []}
        self.bump_Classify_3={'valley': [],
                                'flat': [],
                                'peak': []}
        self.bump_Classify_35={'valley': [],
                                'flat': [],
                                'peak': []}
        self.bump_Classify_4={'valley': [],
                                'flat': [],
                                'peak': []}
        self.bump_Classify_45={'valley': [],
                                'flat': [],
                                'peak': []}
        self.bump_Classify_6={'valley': [],
                                'flat': [],
                                'peak': []}
        # defalut set all_protein



        self.bump_Classify_set = {}

        self.valleyCell = []
        self.flatCell = []
        self.peakCell = []
        self.valley_range_get = ''
        ################################

        self.INTERFACE_DIS_3 = []
        self.INTERFACE_DIS_35 = []
        self.INTERFACE_DIS_4 = []
        self.INTERFACE_DIS_45 = []
        self.INTERFACE_DIS_5 = []
        self.INTERFACE_DIS_55 = []
        self.INTERFACE_DIS_6 = []
        self.INTERFACE_DIS_7 = []
        self.INTERFACE_DIS_75 = []
        self.INTERFACE_DIS_8 = []
        self.INTERFACE_DIS_85 = []
        self.INTERFACE_DIS_9 = []
        self.INTERFACE_DIS_95 = []
        self.INTERFACE_DIS_10 = []


        ################################
        # COLOR VAR
        self.surf_col = '#7CFC00'
        self.protein_col = '#666666'
        self.nucleic_col = '#666666'
        self.bump_col = '#FF3030'
        self.valley_col = '#FF0000'
        self.peak_col = '#0000FF'
        self.flat_col = '#00FF00'

        self.property_col = '#7CFC00'

        self.surf_col_tuple = (124, 252, 0)
        self.valley_col_tuple = (255, 0, 0)
        self.flat_col_tuple = (0, 255, 0)
        self.peak_col_tuple = (0, 0, 255)
        self.property_col_tuple = (125, 250, 0)

        self.protein_col_tuple = (88, 87, 86)
        self.nucleic_col_tuple = (88, 87, 86)

        cmd.set_color('valley_col', self.valley_col_tuple)
        cmd.set_color('flat_col', self.flat_col_tuple)
        cmd.set_color('peak_col', self.peak_col_tuple)

        #info
        self.interface3_lead = []
        self.interface35_lead = []
        self.interface4_lead = []
        self.interface45_lead = []
        self.interface5_lead = []
        self.interface55_lead = []
        self.interface6_lead = []
        self.interface65_lead = []
        self.interface7_lead = []
        self.interface75_lead = []
        self.interface8_lead = []
        self.interface85_lead = []
        self.interface9_lead = []
        self.interface95_lead = []
        self.interface10_lead = []
        ################################
        self.Resn_number = {'ALA': 0,
                            'ARG': 0,
                            'ASN': 0,
                            'ASP': 0,
                            'CYS': 0,
                            'GLN': 0,
                            'GLU': 0,
                            'GLY': 0,
                            'HIS': 0,
                            'ILE': 0,
                            'LEU': 0,
                            'LYS': 0,
                            'MET': 0,
                            'PHE': 0,
                            'PRO': 0,
                            'SER': 0,
                            'THR': 0,
                            'TRP': 0,
                            'TYR': 0,
                            'VAL': 0,
                            }

        self.interface3_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface35_resn_number = {'ALA': 0,
                                        'ARG': 0,
                                        'ASN': 0,
                                        'ASP': 0,
                                        'CYS': 0,
                                        'GLN': 0,
                                        'GLU': 0,
                                        'GLY': 0,
                                        'HIS': 0,
                                        'ILE': 0,
                                        'LEU': 0,
                                        'LYS': 0,
                                        'MET': 0,
                                        'PHE': 0,
                                        'PRO': 0,
                                        'SER': 0,
                                        'THR': 0,
                                        'TRP': 0,
                                        'TYR': 0,
                                        'VAL': 0,
                                        }
        self.interface4_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface45_resn_number = {'ALA': 0,
                                        'ARG': 0,
                                        'ASN': 0,
                                        'ASP': 0,
                                        'CYS': 0,
                                        'GLN': 0,
                                        'GLU': 0,
                                        'GLY': 0,
                                        'HIS': 0,
                                        'ILE': 0,
                                        'LEU': 0,
                                        'LYS': 0,
                                        'MET': 0,
                                        'PHE': 0,
                                        'PRO': 0,
                                        'SER': 0,
                                        'THR': 0,
                                        'TRP': 0,
                                        'TYR': 0,
                                        'VAL': 0,
                                        }
        self.interface5_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface55_resn_number = {'ALA': 0,
                                        'ARG': 0,
                                        'ASN': 0,
                                        'ASP': 0,
                                        'CYS': 0,
                                        'GLN': 0,
                                        'GLU': 0,
                                        'GLY': 0,
                                        'HIS': 0,
                                        'ILE': 0,
                                        'LEU': 0,
                                        'LYS': 0,
                                        'MET': 0,
                                        'PHE': 0,
                                        'PRO': 0,
                                        'SER': 0,
                                        'THR': 0,
                                        'TRP': 0,
                                        'TYR': 0,
                                        'VAL': 0,
                                        }
        self.interface6_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface65_resn_number = {'ALA': 0,
                                        'ARG': 0,
                                        'ASN': 0,
                                        'ASP': 0,
                                        'CYS': 0,
                                        'GLN': 0,
                                        'GLU': 0,
                                        'GLY': 0,
                                        'HIS': 0,
                                        'ILE': 0,
                                        'LEU': 0,
                                        'LYS': 0,
                                        'MET': 0,
                                        'PHE': 0,
                                        'PRO': 0,
                                        'SER': 0,
                                        'THR': 0,
                                        'TRP': 0,
                                        'TYR': 0,
                                        'VAL': 0,
                                        }
        self.interface7_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface75_resn_number = {'ALA': 0,
                                        'ARG': 0,
                                        'ASN': 0,
                                        'ASP': 0,
                                        'CYS': 0,
                                        'GLN': 0,
                                        'GLU': 0,
                                        'GLY': 0,
                                        'HIS': 0,
                                        'ILE': 0,
                                        'LEU': 0,
                                        'LYS': 0,
                                        'MET': 0,
                                        'PHE': 0,
                                        'PRO': 0,
                                        'SER': 0,
                                        'THR': 0,
                                        'TRP': 0,
                                        'TYR': 0,
                                        'VAL': 0,
                                        }
        self.interface8_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface85_resn_number = {'ALA': 0,
                                        'ARG': 0,
                                        'ASN': 0,
                                        'ASP': 0,
                                        'CYS': 0,
                                        'GLN': 0,
                                        'GLU': 0,
                                        'GLY': 0,
                                        'HIS': 0,
                                        'ILE': 0,
                                        'LEU': 0,
                                        'LYS': 0,
                                        'MET': 0,
                                        'PHE': 0,
                                        'PRO': 0,
                                        'SER': 0,
                                        'THR': 0,
                                        'TRP': 0,
                                        'TYR': 0,
                                        'VAL': 0,
                                        }
        self.interface9_resn_number = {'ALA': 0,
                                       'ARG': 0,
                                       'ASN': 0,
                                       'ASP': 0,
                                       'CYS': 0,
                                       'GLN': 0,
                                       'GLU': 0,
                                       'GLY': 0,
                                       'HIS': 0,
                                       'ILE': 0,
                                       'LEU': 0,
                                       'LYS': 0,
                                       'MET': 0,
                                       'PHE': 0,
                                       'PRO': 0,
                                       'SER': 0,
                                       'THR': 0,
                                       'TRP': 0,
                                       'TYR': 0,
                                       'VAL': 0,
                                       }
        self.interface95_resn_number = {'ALA': 0,
                                        'ARG': 0,
                                        'ASN': 0,
                                        'ASP': 0,
                                        'CYS': 0,
                                        'GLN': 0,
                                        'GLU': 0,
                                        'GLY': 0,
                                        'HIS': 0,
                                        'ILE': 0,
                                        'LEU': 0,
                                        'LYS': 0,
                                        'MET': 0,
                                        'PHE': 0,
                                        'PRO': 0,
                                        'SER': 0,
                                        'THR': 0,
                                        'TRP': 0,
                                        'TYR': 0,
                                        'VAL': 0,
                                        }
        self.interface10_resn_number = {'ALA': 0,
                                        'ARG': 0,
                                        'ASN': 0,
                                        'ASP': 0,
                                        'CYS': 0,
                                        'GLN': 0,
                                        'GLU': 0,
                                        'GLY': 0,
                                        'HIS': 0,
                                        'ILE': 0,
                                        'LEU': 0,
                                        'LYS': 0,
                                        'MET': 0,
                                        'PHE': 0,
                                        'PRO': 0,
                                        'SER': 0,
                                        'THR': 0,
                                        'TRP': 0,
                                        'TYR': 0,
                                        'VAL': 0,
                                        }
        ###############################


        self.Amino_acid = ['ALA',
                           'ARG',
                           'ASN',
                           'ASP',
                           'CYS',
                           'GLN',
                           'GLU',
                           'GLY',
                           'HIS',
                           'ILE',
                           'LEU',
                           'LYS',
                           'MET',
                           'PHE',
                           'PRO',
                           'SER',
                           'THR',
                           'TRP',
                           'TYR',
                           'VAL', ]

        self.NegativeCharge_res = ['ASP', 'GLU']
        self.PostiveCharge_res = ['LYS', 'ARG', 'HIS']
        self.None_Charge_res = ['ALA', 'ASN', 'CYS', 'GLN', 'GLY', 'ILE', 'LEU', 'MET', 'PHE', 'PRO', 'SER', 'THR',
                                'TRP', 'TYR', 'VAL']
        self.Hydrophobicity_res = ['ALA', 'GLY', 'VAL', 'ILE', 'LEU', 'PHE', 'MET']
        self.Hydrophilicity_res = ['ARG', 'LYS', 'HIS', 'GLU', 'ASP', 'ASN', 'GLN', 'THR', 'SER', 'CYS']

        # GUI
        ##########
        self.dialog = Pmw.Dialog(self.parent,
                                 buttons=('Show interface h-bonds','Hide nucleic', 'Show nucleic', 'Hide HOH','Show HOH','Exit'),
                                 title='InPrNa1.0',
                                 command=self.execute
                                 )

        Pmw.setbusycursorattributes(self.dialog.component('hull'))

        # main label
        Main_Label = Tkinter.Label(self.dialog.interior(),
                                   text='\nInPrNa1.0\n Natural Science Foundation of Henan province 182300410368\n',
                                   background='black', foreground='green'
                                   )
        Main_Label.pack(expand=1, fill='both', padx=10, pady=5)

        ############
        # create NoteBook
        ############
        self.Notebook = Pmw.NoteBook(self.dialog.interior(), )
        self.Notebook.pack(fill='both', expand=1, padx=25, pady=15)
        #########
        # Visualization TAB
        #########
        # interface labelframe
        page = self.Notebook.add('Visualization')
        Interface_LF = ttk.Labelframe(page, text='Interface setting')
        page.columnconfigure(1, weight=1)
        page.columnconfigure(0, weight=1)
        page.columnconfigure(2, weight=1)
        page.rowconfigure(1, weight=1)


        Interface_LF.grid(sticky='NESW', row=0, column=0, padx=10, pady=5)

        inter_col_lb = Tkinter.Label(Interface_LF, text='Interface Color:')
        self.inter_col_but = Tkinter.Button(Interface_LF, bg=self.surf_col,
                                            activebackground=self.surf_col,
                                            command=lambda :self.ch_inter_col(self.INTERFACE_CONTENT))
        # mode setting
        interface_mod_Lb = Tkinter.Label(Interface_LF, text='Show Mode:')
        def interface_Cb_ch(*args):
            self.interface_mod = self.interface_mod_Cb.get()
            # cmd.disable("INTERFACE")
            # cmd.show(self.interface_mod_Cb.get(),"INTERFACE")



        self.interface_mod_Cb = ttk.Combobox(Interface_LF, width=10)
        self.interface_mod_Cb["values"] = (
            "sphere", "cartoon", "lines", "sticks", "riddon", "dots", "mesh", "surface", "nonbonded", "nb_pheres")
        self.interface_mod_Cb.current(0)
        self.interface_mod_Cb.bind("<<ComboboxSelected>>", interface_Cb_ch)

        # label button grid
        inter_col_lb.grid(sticky='E', column=0, row=0, padx=5, pady=1)
        self.inter_col_but.grid(sticky='NESW', column=1, row=0, padx=5, pady=1)

        interface_mod_Lb.grid(sticky='WE', column=0, row=2, padx=5, pady=1)
        self.interface_mod_Cb.grid(sticky='WE', column=1, row=2, padx=5, pady=1)

        # interface_dis

        Interface_dis_setting_LB = Tkinter.Label(Interface_LF, text='Interface DIS:')

        def interface_dis_cb_ch(args):
            self.DIS = self.interface_dis_cb.get()
            #print self.DIS

        self.interface_dis_cb = ttk.Combobox(Interface_LF, width=10)
        self.interface_dis_cb["values"] = (6, 3, 3.5, 4, 4.5, 5, 5.5,  6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10)

        self.interface_dis_cb.current(0)
        self.interface_dis_cb.bind("<<ComboboxSelected>>",interface_dis_cb_ch)

        self.interface_dis_but = Tkinter.Button(Interface_LF,text='APPLY', command=self.interface_dis_ch)
        self.interface_dis_but.grid(sticky='WE', column=2, row=3, padx=5, pady=1)

        # self.show_apbs_color = Tkinter.Button(Interface_LF,text='show h_bonds dash', command=self.show_apbs_col)
        # self.show_apbs_color.grid(sticky='WE', column=2, row=4, padx=5, pady=1)

        Interface_dis_setting_LB.grid(sticky='WE', column=0, row=3, padx=5, pady=1)
        self.interface_dis_cb.grid(sticky='WE', column=1, row=3, padx=5, pady=1)

        # Vis_page big entry
        self.Visualization_ScroT = tkst.ScrolledText(page, width=80, height=10)
        self.Visualization_ScroT.grid(sticky='WSNE', columnspan=3, rowspan=2, padx=15)
        ###################################################################
        #protein setting
        Protein_LF = ttk.LabelFrame(page,text='protein setting')
        Protein_LF.grid(sticky='NESW', row=0, column=1, padx=10, pady=5)

        protein_col_lb = Tkinter.Label(Protein_LF, text='Protein Color:')
        self.protein_col_but = Tkinter.Button(Protein_LF, bg=self.protein_col,
                                            activebackground=self.protein_col,
                                            command=lambda :self.ch_protein_col())
        # mode setting
        protein_mod_Lb = Tkinter.Label(Protein_LF, text='Show Mode:')
        ################################################################################################                  protein
        def protein_Cb_ch(*args):
            self.protein_mod = self.protein_mod_Cb.get()
            cmd.hide("everything", "protein")
            cmd.show(self.protein_mod_Cb.get(), "protein")
            cmd.hide("everything", "interface")

        self.protein_mod_Cb = ttk.Combobox(Protein_LF, width=10)
        self.protein_mod_Cb["values"] = (
            "sphere", "cartoon", "lines", "sticks", "riddon", "dots", "mesh", "surface", "nonbonded", "nb_pheres")
        self.protein_mod_Cb.current(0)
        self.protein_mod_Cb.bind("<<ComboboxSelected>>", protein_Cb_ch)

        # label button grid
        protein_col_lb.grid(sticky='E', column=0, row=0, padx=5, pady=1)
        self.protein_col_but.grid(sticky='NESW', column=1, row=0, padx=5, pady=1)

        protein_mod_Lb.grid(sticky='WE', column=0, row=2, padx=5, pady=1)
        self.protein_mod_Cb.grid(sticky='WE', column=1, row=2, padx=5, pady=1)

####################################
		# nucleic setting
####################################

        nucleic_LF = ttk.LabelFrame(page, text='nucleic setting')
        nucleic_LF.grid(sticky='NESW', row=0, column=2, padx=10, pady=5)

        nucleic_col_lb = Tkinter.Label(nucleic_LF, text='nucleic color:')
        self.nucleic_col_but = Tkinter.Button(nucleic_LF, bg=self.nucleic_col,
                                              activebackground=self.nucleic_col,
                                              command=lambda: self.ch_nucleic_col())
        # mode setting
        nucleic_mod_Lb = Tkinter.Label(nucleic_LF, text='Show mode:')
        nucleic_cartoon_Lb = Tkinter.Label(nucleic_LF, text='nucleic cartoon mode:')

        def nucleic_Cb_ch(*args):
            self.protein_mod = self.nucleic_mod_Cb.get()
            cmd.hide("everything", "nucleic")
            # if self.nucleic_mod_Cb
            cmd.show(self.nucleic_mod_Cb.get(), "nucleic")

        def nucleic_cb_cartoon(*args):
            words = self.nucleic_cartoon_mod.get()
            number = int(words[-1:])
            print number, words[:-2]
            cmd.set(words[:-2], number)

        self.nucleic_mod_Cb = ttk.Combobox(nucleic_LF, width=18)
        self.nucleic_mod_Cb["values"] = (
            "sphere", "cartoon", "lines", "sticks", "riddon", "dots", "mesh", "surface", "nonbonded", "nb_pheres")
        self.nucleic_mod_Cb.current(0)
        self.nucleic_mod_Cb.bind("<<ComboboxSelected>>", nucleic_Cb_ch)

        self.nucleic_cartoon_mod = ttk.Combobox(nucleic_LF, width=18)
        self.nucleic_cartoon_mod["values"] = (
            "cartoon_ring_mode_0", "cartoon_ring_mode_1", "cartoon_ring_mode_2", "cartoon_ring_mode_3",
            "cartoon_ring_finder_0", "cartoon_ring_finder_1", "cartoon_ring_finder_2", "cartoon_ring_finder_3",
            "cartoon_ladder_mode_0", "cartoon_ladder_mode_1"
        )
        self.nucleic_cartoon_mod.current(0)
        self.nucleic_cartoon_mod.bind("<<ComboboxSelected>>", nucleic_cb_cartoon)

        # label button grid
        nucleic_col_lb.grid(sticky='WE', column=0, row=0, padx=5, pady=1)
        self.nucleic_col_but.grid(sticky='WE', column=1, row=0, padx=5, pady=1)

        nucleic_mod_Lb.grid(sticky='WE', column=0, row=2, padx=5, pady=1)
        self.nucleic_mod_Cb.grid(sticky='WE', column=1, row=2, padx=5, pady=1)

        nucleic_cartoon_Lb.grid(sticky='WE', column=0, row=3, padx=5, pady=1)
        self.nucleic_cartoon_mod.grid(sticky='WE', column=1, row=3, padx=5, pady=1)

        #########
        # Amino acid TAB
        #########

        page = self.Notebook.add('Amino acid ')
        Amino_acid_property_LF = ttk.LabelFrame(page, text="Amino acid property setting:")
        Amino_acid_property_LF.pack(fill='both', expand=True, padx=10, pady=5)

        Amino_acid_property_Cb = ttk.Combobox(Amino_acid_property_LF, width=15)
        Amino_acid_property_Cb["values"] = (
            "Hydrophobicity", "Hydrophilicity", "Positive charge", "Negative charge", "None charge")
        Amino_acid_property_Cb.current(0)
        # combox
        self.property = Amino_acid_property_Cb.get()

        def PropertyClick(args):
            self.property = Amino_acid_property_Cb.get()

        Amino_acid_property_Cb.bind("<<ComboboxSelected>>", PropertyClick)

        self.ch_Prooerty_col_but = Tkinter.Button(Amino_acid_property_LF, bg=self.property_col,
                                                  activebackground=self.property_col,
                                                  command=self.ch_propert_col)

        Amino_acid_property_But = Tkinter.Button(Amino_acid_property_LF, text='Apply', command=self.property_but)
        Amino_acid_property_Cb.grid(sticky='WE', row=0, column=0, padx=5, pady=5)
        self.ch_Prooerty_col_but.grid(sticky='WE', row=0, column=1, padx=5, pady=5)
        Amino_acid_property_But.grid(sticky='WE', row=0, column=2, padx=5, pady=5)

        Amino_acid_property_LF.columnconfigure(2, weight=9)
        Amino_acid_property_LF.columnconfigure(1, weight=9)
        Amino_acid_property_LF.columnconfigure(0, weight=9)

        # Amino_acid_inf_Ent = Entry(page,state='readonly')
        # Amino_acid_inf_Ent.pack(fill='both',expand=True,padx=10,pady=5)


        self.Amino_acid_inf_ScroT = tkst.ScrolledText(page, width=80, height=10)
        self.Amino_acid_inf_ScroT.pack(fill='both', expand=True, padx=10, pady=5)

        self.Notebook.setnaturalsize()


        #########
        # BUMP TAB
        #########
        page  = self.Notebook.add('Bump')

        Bump_LF = ttk.Labelframe(page, text='concavity and convex :')
        Bump_LF.columnconfigure(1, weight=9)
        Bump_LF.pack(expand=1, fill='both', padx=10, pady=5)



        #valley
        valley_col_lb = Tkinter.Label(Bump_LF, text='Valley:')
        self.ch_valley_col_but = Tkinter.Button(Bump_LF, bg=self.valley_col,
                                               activebackground=self.valley_col,
                                               command=self.ch_valley_col)
        #range select
        def valley_range_cb(args):
            self.valley_range_get = self.valley_range.get()
            print self.valley_range_get
            self.bump_Classify_valley = self.bump_Classify_set[self.valley_range_get]

        self.valley_range = ttk.Combobox(Bump_LF,width=10)
        self.valley_range["values"] = ("all_protein","3angstrom","3.5angstrom","4angstrom","4.5angstrom","6angstrom")
        self.valley_range.current(0)
        self.valley_range.bind("<<ComboboxSelected>>",valley_range_cb)

        def valley_Cb_ch(*args):
            self.Valley_mod = self.Valley_mod_Cb.get()

        self.Valley_mod_Cb = ttk.Combobox(Bump_LF, width=10)
        self.Valley_mod_Cb["values"] = (
            "sphere", "cartoon", "lines", "sticks", "riddon", "dots", "mesh", "surface", "nonbonded", "nb_pheres")
        self.Valley_mod_Cb.current(0)
        self.Valley_mod_Cb.bind("<<ComboboxSelected>>", valley_Cb_ch)


        peak_col_lb = Tkinter.Label(Bump_LF, text='peak :')
        self.ch_peak_col_but = Tkinter.Button(Bump_LF, bg=self.peak_col,
                                              activebackground=self.peak_col,
                                              command=self.ch_peak_col)
        def peak_range_cb(*args):
            self.peak_range_get = self.peak_range.get()
            print self.peak_range_get
            self.bump_Classify_peak = self.bump_Classify_set[self.peak_range_get]
            #print self.bump_Classify_peak

        self.peak_range = ttk.Combobox(Bump_LF,width=10)
        self.peak_range["values"] = ("all_protein","3angstrom","3.5angstrom","4angstrom","4.5angstrom","6angstrom")
        self.peak_range.current(0)
        self.peak_range.bind("<<ComboboxSelected>>",peak_range_cb)

        def peak_Cb_ch(*args):
            self.Valley_mod = self.peak_mod_Cb.get()

        self.peak_mod_Cb = ttk.Combobox(Bump_LF, width=10)
        self.peak_mod_Cb["values"] = (
            "sphere", "cartoon", "lines", "sticks", "riddon", "dots", "mesh", "surface", "nonbonded", "nb_pheres")
        self.peak_mod_Cb.current(0)
        self.peak_mod_Cb.bind("<<ComboboxSelected>>", peak_Cb_ch)


        #flat
        flat_col_lb = Tkinter.Label(Bump_LF, text='flat :')
        self.ch_flat_col_but = Tkinter.Button(Bump_LF, bg=self.flat_col,
                                              activebackground=self.flat_col,
                                              command=self.ch_flat_col)
        def flat_range_cb(*args):
            self.flat_range_get = self.flat_range.get()
            print self.flat_range_get
            self.bump_Classify_flat = self.bump_Classify_set[self.flat_range_get]
            #print self.bump_Classify_flat

        self.flat_range = ttk.Combobox(Bump_LF,width=10)
        self.flat_range["values"] = ("all_protein","3angstrom","3.5angstrom","4angstrom","4.5angstrom","6angstrom")
        self.flat_range.current(0)
        self.flat_range.bind("<<ComboboxSelected>>",flat_range_cb)

        def flat_Cb_ch(*args):
            self.flat_mod = self.flat_mod_Cb.get()

        self.flat_mod_Cb = ttk.Combobox(Bump_LF, width=10)
        self.flat_mod_Cb["values"] = (
            "sphere", "cartoon", "lines", "sticks", "riddon", "dots", "mesh", "surface", "nonbonded", "nb_pheres")
        self.flat_mod_Cb.current(0)
        self.flat_mod_Cb.bind("<<ComboboxSelected>>", flat_Cb_ch)

        cofirm_button = Tkinter.Button(Bump_LF,text='confirm setting',command=self.bump_confirm)

        #grid
        valley_col_lb.grid(sticky='W', column=0, row=0, padx=5, pady=1)
        self.ch_valley_col_but.grid(sticky='WSNE', column=1, row=0, padx=5, pady=1)
        self.valley_range.grid(sticky='WSNE', column=2, row=0, padx=5, pady=1)
        self.Valley_mod_Cb.grid(sticky='E', column=3, row=0, padx=5, pady=1)

        peak_col_lb.grid(sticky='W', column=0, row=1, padx=5, pady=1)
        self.ch_peak_col_but.grid(sticky='WSNE', column=1, row=1, padx=5, pady=1)
        self.peak_range.grid(sticky='WSNE', column=2, row=1, padx=5, pady=1)
        self.peak_mod_Cb.grid(sticky='E', column=3, row=1, padx=5, pady=1)

        flat_col_lb.grid(sticky='W', column=0, row=2, padx=5, pady=1)
        self.ch_flat_col_but.grid(sticky='WSNE', column=1, row=2, padx=5, pady=1)
        self.flat_range.grid(sticky='WSNE', column=2, row=2, padx=5, pady=1)
        self.flat_mod_Cb.grid(sticky='E', column=3, row=2, padx=5, pady=1)


        cofirm_button.grid(sticky= 'E',column=3, row=3, padx=5, pady=1)
    def Open_PDB_content(self, pdb_file_name):
        file_handle = open(pdb_file_name, 'r')
        counter = 0
        atom_content_dir = {}
        for file_content in file_handle:
            if file_content[0:4] == 'ATOM':
                if file_content[17:20] != ' DA' and \
                                file_content[17:20] != ' DT' and \
                                file_content[17:20] != ' DG' and \
                                file_content[17:20] != ' DC' and \
                                file_content[17:20] != '  A' and \
                                file_content[17:20] != '  C' and \
                                file_content[17:20] != '  G' and \
                                file_content[17:20] != '  T' and \
                                file_content[17:20] != '  U' and \
                                file_content[17:20] != '  I':
                    atom_content_dir[counter] = file_content
                    counter = counter + 1
        # print counter
        return atom_content_dir

    def calcu_dis(self, coord_1, coord_2):

        coord_1_X = float(coord_1[0])
        coord_1_Y = float(coord_1[1])
        coord_1_Z = float(coord_1[2])
        coord_2_X = float(coord_2[0])
        coord_2_Y = float(coord_2[1])
        coord_2_Z = float(coord_2[2])

        Euclid_Dis = numpy.sqrt(
            ((coord_1_X - coord_2_X) ** 2) + ((coord_1_Y - coord_2_Y) ** 2) + ((coord_1_Z - coord_2_Z) ** 2))

        return Euclid_Dis

    def property_but(self):
        color_Tuple = self.property_col_tuple

        if self.property == 'Hydrophobicity':
            self.Amino_acid_inf_ScroT.delete(1.0, Tkinter.END)
            self.Amino_acid_inf_ScroT.insert(1.0, 'Hydrophobicity:\n')

            for key in self.Hydrophobicity_res:
                self.Amino_acid_inf_ScroT.insert(Tkinter.INSERT, key + ' ')
                self.Amino_acid_inf_ScroT.insert(Tkinter.INSERT, str(self.Resn_number[key]) + '\n')
            resn = self.Sel_Resn_list(self.Hydrophobicity_res)

            # pymol
            cmd.set_color('hydrophobicity_col', color_Tuple)
            cmd.select('hydrophobicity', resn)
            cmd.color('hydrophobicity_col', 'hydrophobicity')

        if self.property == 'Hydrophilicity':
            self.Amino_acid_inf_ScroT.delete(1.0, Tkinter.END)
            self.Amino_acid_inf_ScroT.insert(1.0, 'Hydrophilicity:\n')

            for key in self.Hydrophilicity_res:
                self.Amino_acid_inf_ScroT.insert(Tkinter.INSERT, key + ' ')
                self.Amino_acid_inf_ScroT.insert(Tkinter.INSERT, str(self.Resn_number[key]) + '\n')

            resn = self.Sel_Resn_list(self.Hydrophilicity_res)
            # pymol
            cmd.set_color('Hydrophilicity_col', color_Tuple)
            cmd.select('Hydrophilicity', resn)
            cmd.color('Hydrophilicity_col', 'Hydrophilicity')

        if self.property == 'Positive charge':
            self.Amino_acid_inf_ScroT.delete(1.0, Tkinter.END)
            self.Amino_acid_inf_ScroT.insert(1.0, 'Postive charge:\n')
            for key in self.PostiveCharge_res:
                self.Amino_acid_inf_ScroT.insert(Tkinter.INSERT, key + ' ')
                self.Amino_acid_inf_ScroT.insert(Tkinter.INSERT, str(self.Resn_number[key]) + '\n')

            # pymol
            resn = self.Sel_Resn_list(self.PostiveCharge_res)
            cmd.set_color('Postive_col', color_Tuple)
            cmd.select('positive_charge', resn)
            cmd.color('Postive_col', 'positive_charge')

        if self.property == 'Negative charge':
            self.Amino_acid_inf_ScroT.delete(1.0, Tkinter.END)
            self.Amino_acid_inf_ScroT.insert(1.0, 'Negative charge:\n')
            for key in self.NegativeCharge_res:
                self.Amino_acid_inf_ScroT.insert(Tkinter.INSERT, key + ' ')
                self.Amino_acid_inf_ScroT.insert(Tkinter.INSERT, str(self.Resn_number[key]) + '\n')

            # pymol
            resn = self.Sel_Resn_list(self.NegativeCharge_res)
            cmd.set_color('Negative_col', color_Tuple)
            cmd.select('Negative_charge', resn)
            cmd.color('Negative_col', 'Negative_charge')

        if self.property == 'None charge':
            self.Amino_acid_inf_ScroT.delete(1.0, Tkinter.END)
            self.Amino_acid_inf_ScroT.insert(1.0, 'None charge:\n')
            for key in self.None_Charge_res:
                self.Amino_acid_inf_ScroT.insert(Tkinter.INSERT, key + ' ')
                self.Amino_acid_inf_ScroT.insert(Tkinter.INSERT, str(self.Resn_number[key]) + '\n')

            # pymol
            resn = self.Sel_Resn_list(self.None_Charge_res)
            cmd.set_color('None_col', color_Tuple)
            cmd.select('None_charge', resn)
            cmd.color('None_col', 'None_charge')



            # cmd.set_color('Negative_col',Negative_col)
            # cmd.set_color('NoneCharge_col',NoneCharge_col)
            # for key in self.Amino_acid:
            #    if self.Charge[key] == 0:
            #        cmd.select('ChargeTemp', 'resn ' + key)
            #        cmd.color('NoneCharge_col', 'Charge')
            #    if self.Charge[key] == 1:
            #        cmd.select('ChargeTemp','resn '+ key)
            #        cmd.color('Postive_col','ChargeTemp')
            #    if self.Charge[key] == -1:
            #        cmd.select('ChargeTemp','resn '+ key)
            #        cmd.color('Negative_col','ChargeTemp')

    def interface_dis_ch(self):
        DIS = float(self.DIS)
        cmd.show(self.protein_mod_Cb.get(),"protein")
        cmd.hide("everything", "interface")
        #print DIS
        try:
            if DIS == 3:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_3,self.interface3_resn_number,self.interface3_lead)
            if DIS == 3.5:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_35,self.interface35_resn_number,self.interface35_lead)
            if DIS == 4:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_4,self.interface4_resn_number,self.interface4_lead)
            if DIS == 4.5:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_45, self.interface45_resn_number,self.interface45_lead)
            if DIS == 5:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_5, self.interface5_resn_number,self.interface5_lead)
            if DIS == 5.5:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_55, self.interface55_resn_number,self.interface55_lead)
            if DIS == 6.5:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_65, self.interface65_resn_number,self.interface65_lead)
            if DIS == 7:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_7, self.interface7_resn_number,self.interface7_lead)
            if DIS == 7.5:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_75, self.interface75_resn_number,self.interface75_lead)
            if DIS == 8:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_8, self.interface8_resn_number,self.interface8_lead)
            if DIS == 8.5:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_85, self.interface85_resn_number,self.interface85_lead)
            if DIS == 9:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_9, self.interface9_resn_number,self.interface9_lead)
            if DIS == 9.5:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_95, self.interface95_resn_number,self.interface95_lead)
            if DIS == 10:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_10, self.interface10_resn_number,self.interface10_lead)
            if DIS == 6:
                self.INFORMATION_SHOW(self.INTERFACE_DIS_6,self.interface6_resn_number,self.interface6_lead)
            # cmd.hide("everything", "interface")
        except :
            print 'no data input'
        # cmd.disable("INTERFACE")
        # cmd.hide("everything", "interface")
        cmd.show(self.interface_mod, "INTERFACE")
        cmd.hide('everything', 'interface')

    def show_hbonds_but(self):
        cmd.set("h_bond_cutoff_center", "3.6")
        cmd.set("h_bond_cutoff_edge", "3.2")
        cmd.distance("interface_nucleic_hbonds", "interface", "nucleic", mode="2")

    #
    def show_apbs_col(self):
        pymol.color_list = []
        pymol.resn_num = []
        cmd.hide("everything", "nucleic")
        # cmd.hide("everything", "protein")
        cmd.iterate('interface', 'pymol.color_list.append(cmd.get_color_tuple(color))')
        cmd.iterate('INTERFACE', 'pymol.resn_num.append(resn)')
        counter = 0
        for key in pymol.resn_num:
            cmd.set_color('temp', pymol.color_list[counter])
            cmd.color('temp', 'resn '+key)
            counter += 1


        # print pymol.color_list

    #
    def ch_propert_col(self):
        color_tuple, color = tkColorChooser.askcolor(color=self.property_col)
        if color_tuple is not None and color is not None:
            self.property_col_tuple = color_tuple
            self.property_col = color
            self.ch_Prooerty_col_but['bg'] = self.property_col
            self.ch_Prooerty_col_but['activebackground'] = self.property_col
            self.ch_Prooerty_col_but.update()

    def ch_inter_col(self,INTERFACE_CONTENT):
        #print INTERFACE_CONTENT
        color_tuple, color = tkColorChooser.askcolor(color=self.surf_col)
        if color_tuple is not None and color is not None:
            # self.surf_col_R, self.surf_col_G,self.surf_col_B= color_tuple
            self.surf_col_tuple = color_tuple
            self.surf_col = color
            # print self.surf_col
            self.inter_col_but['bg'] = self.surf_col
            self.inter_col_but['activebackground'] = self.surf_col
            self.inter_col_but.update()
            cmd.set_color('surf_col', self.surf_col_tuple)
            cmd.color('surf_col', 'INTERFACE1')

    def ch_protein_col(self):
        #print INTERFACE_CONTENT
        color_tuple, color = tkColorChooser.askcolor(color=self.protein_col)
        if color_tuple is not None and color is not None:
            # self.surf_col_R, self.surf_col_G,self.surf_col_B= color_tuple
            self.protein_col_tuple = color_tuple
            self.protein_col = color
            # print self.surf_col
            self.protein_col_but['bg'] = self.protein_col
            self.protein_col_but['activebackground'] = self.protein_col
            self.protein_col_but.update()
            cmd.set_color('protein_col', self.protein_col_tuple)
            cmd.color('protein_col', 'protein')

    def ch_nucleic_col(self):
        #print INTERFACE_CONTENT
        color_tuple, color = tkColorChooser.askcolor(color=self.nucleic_col)
        if color_tuple is not None and color is not None:
            # self.surf_col_R, self.surf_col_G,self.surf_col_B= color_tuple
            self.nucleic_col_tuple = color_tuple
            self.nucleic_col = color
            # print self.surf_col
            self.nucleic_col_but['bg'] = self.nucleic_col
            self.nucleic_col_but['activebackground'] = self.nucleic_col
            print (self.nucleic_col_tuple)
            self.nucleic_col_but.update()
            cmd.set_color('nucleic_col', self.nucleic_col_tuple)
            cmd.color('nucleic_col', 'nucleic')



    def INFORMATION_SHOW(self,INTERFACE_CONTENT,interface_resn_number,lead_info):
        #print 'step2'
        #print INTERFACE_CONTENT
        chain = self.Sel_Chain(INTERFACE_CONTENT)
        resi = self.Sel_Resi(INTERFACE_CONTENT)
        resn = self.Sel_Resn(INTERFACE_CONTENT)


        # get interface resn
        resn_list = []
        chain_list = []
        resi_list = []
        for i in INTERFACE_CONTENT:
            resn_list.append(i[17:20])
            resi_list.append(i[22:26])
            chain_list.append(i[21])
        resn_list = list(set(resn_list))
        chain_list = list(set(chain_list))
        resi_list = list(set(resi_list))

        self.Visualization_ScroT.delete(1.0, Tkinter.END)
        self.Visualization_ScroT.insert(1.0, 'INTERFACE :\n')

        self.Visualization_ScroT.insert(Tkinter.INSERT,
                                        'There are the total of kinds of amino acids in the interface:\n')
        for key in resn_list:
            self.Visualization_ScroT.insert(Tkinter.INSERT, key + ' ')
            self.Visualization_ScroT.insert(Tkinter.INSERT, str(interface_resn_number[key]) + '  ')

        # info
        self.Visualization_ScroT.insert(Tkinter.INSERT, '\n\nNucleic acid atom closest to the interface amino acid residue:\n (Amino acid residue -- Nucleic acid atom)\n')
        for key in lead_info:
            self.Visualization_ScroT.insert(Tkinter.INSERT, key+"\n")

        self.Visualization_ScroT.insert(Tkinter.INSERT,'\nInteface(pdb origin data):\n')
        interface_vis = []
        for key in INTERFACE_CONTENT:
            if key not in interface_vis:
                interface_vis.append(key)
                self.Visualization_ScroT.insert(Tkinter.INSERT,key+'\n')
        #print self.surf_col_tuple

        # cmd.select("interface", resn + ' and ' + resi + ' and ' + chain)
        self.selector(INTERFACE_CONTENT,"interface")
        # print 111111111
        cmd.hide('everything','interface')
        cmd.delete("INTERFACE1")
        cmd.create("INTERFACE1", resn + ' and ' + resi + ' and ' + chain)
        cmd.enable("INTERFACE1")
        cmd.hide("everything","INTERFACE1")
        cmd.show(self.interface_mod,"INTERFACE1")
        cmd.color('gray')

        #cmd.extract("interface","interface")

        cmd.set_color('surf_col', self.surf_col_tuple)
        cmd.color('surf_col', 'INTERFACE1')
        # print 2222
        # cmd.hide('everything', 'interface')


    def ch_valley_col(self):
        color_tuple, color = tkColorChooser.askcolor(color=self.valley_col)
        if color_tuple is not None and color is not None:
            self.valley_col_tuple = color_tuple
            self.valley_col = color
            self.ch_valley_col_but['bg'] = self.valley_col
            self.ch_valley_col_but['activebackground'] = self.valley_col
            self.ch_valley_col_but.update()


            #cmd.select("valley", resn + ' and ' + resi + ' and ' + chain)
            cmd.set_color('valley_col', self.valley_col_tuple)
            #self.select_bump('valley')
            cmd.color('valley_col', 'valley')

    def ch_flat_col(self):
        color_tuple, color = tkColorChooser.askcolor(color=self.flat_col)
        if color_tuple is not None and color is not None:
            self.flat_col_tuple = color_tuple
            self.flat_col = color
            self.ch_flat_col_but['bg'] = self.flat_col
            self.ch_flat_col_but['activebackground'] = self.flat_col
            self.ch_flat_col_but.update()
            cmd.set_color('flat_col', self.flat_col_tuple)
            cmd.color('flat_col', 'flat')


    def ch_peak_col(self):
        color_tuple, color = tkColorChooser.askcolor(color=self.peak_col)
        if color_tuple is not None and color is not None:
            self.peak_col_tuple = color_tuple
            self.peak_col = color
            self.ch_peak_col_but['bg'] = self.peak_col
            self.ch_peak_col_but['activebackground'] = self.peak_col
            self.ch_peak_col_but.update()
            cmd.set_color('peak_col', self.peak_col_tuple)
            cmd.color('peak_col', 'peak')


    def bump_confirm(self):

        cmd.color('gray')
        # cmd.hide("everything",'protein')
        cmd.disable('INTERFACE1')

        self.select_bump()
        cmd.delete("protein1")

        ############
        cmd.show(self.protein_mod,"protein")
        cmd.hide("everything", 'valley')
        cmd.hide("everything", 'flat')
        cmd.hide("everything", 'peak')
        cmd.show(self.Valley_mod_Cb.get(), "valley")
        cmd.show(self.flat_mod_Cb.get(), "flat")
        cmd.show(self.peak_mod_Cb.get(), "peak")
        cmd.color('valley_col', 'valley')
        cmd.color('flat_col', 'flat')
        cmd.color('peak_col', 'peak')
        ###########
        cmd.create("protein1","protein")
        cmd.enable("protein1")
        cmd.hide("everything", 'protein')


    def select_bump(self):
        #valley
         try:
             # cmd.select("valley", resn + ' and ' + resi + ' and ' + chain)
             self.selector(self.bump_Classify_valley['valley'],"valley")

             print 'succceed'
         except:
             print "no  valley data input "
        #flat
         # chain = self.Sel_Chain(self.bump_Classify_flat['flat'])
         # resi = self.Sel_Resi(self.bump_Classify_flat['flat'])
         # resn = self.Sel_Resn(self.bump_Classify_flat['flat'])
         try:

             # cmd.select("flat", resn + ' and ' + resi + ' and ' + chain)
             self.selector(self.bump_Classify_flat['flat'],"flat")

         except:
             print "no flat data input"
        #peak
         # chain = self.Sel_Chain(self.bump_Classify_peak['peak'])
         # resi = self.Sel_Resi(self.bump_Classify_peak['peak'])
         # resn = self.Sel_Resn(self.bump_Classify_peak['peak'])
         try:
             self.selector(self.bump_Classify_peak['peak'],"peak")
             # cmd.select("peak", resn + ' and ' + resi + ' and ' + chain)

         except:
             print "no peak data input "







    ####################
    # main
    ####################
    #######################################
    # interface related
    #######################################

    def Sel_Chain(self, content):
        chain = ''
        mark = 0
        con_list = []
        for i in content:
            con_list.append(i[21])
        new_list = list(set(con_list))
        # print new_list
        for string in new_list:
            if mark == 0:
                chain = chain + string
                mark += 1
            else:
                chain = chain + '+' + string
                mark += 1
        chain = 'chain ' + chain.replace(' ', '')
        # print chain
        return chain

    def Sel_Resi(self, content):
        resi = ''
        con_list = []
        for i in content:
            con_list.append(i[22:26])
        new_list = list(set(con_list))
        # print new_list
        mark = 0
        for string in new_list:
            if mark == 0:
                resi = resi + string
                mark += 1
            else:
                resi = resi + '+' + string
                mark += 1
        resi = 'resi ' + resi.replace(' ', '')
        # print resi
        return resi

    def Sel_Resn(self, content):

        resn = 'resn '
        con_list = []
        for i in content:
            con_list.append(i[17:20])
        new_list = list(set(con_list))
        mark = 0
        for string in new_list:
            if mark == 0:
                resn = resn + string
                mark += 1
            else:
                resn = resn + '+' + string
                mark += 1
        # print resn
        return resn

    def Sel_Resn_list(self, content):
        resn = 'resn '
        con_list = []
        for i in content:
            con_list.append(i)
        new_list = list(set(con_list))
        mark = 0
        for string in new_list:
            if mark == 0:
                resn = resn + string
                mark += 1
            else:
                resn = resn + '+' + string
                mark += 1
        # print resn
        return resn

    def selector(self, content, sele_name):
        cmd.delete(sele_name)
        for i in content:
            # con_list.append(i[17:20])
            cmd.select(sele_name, ' resn ' + i[17:20] + ' and  resi' + i[22:26] + ' and chain ' + i[21], merge=1)

    # def GetPDBFilePath(self):
    #     self.pdbfile = tkFileDialog.askopenfilename()
    #     self.pdb_file_path.set(pdbfile)
    #     # print filePathVar.get()

    def LoadPDB(self):
        if self.pdb_file_path is not None:
            cmd.load(self.pdb_file_path.get())
            cmd.color('gray')
            cmd.show('sphere')
            ############
            ## Main
            ###########
            self.interface_content = self.calcu_durg_pdb_interface(self.pdb_file_path.get())
            # print self.Resn_number
            self.BumpClassify(self.interface_content, self.pdb_file_path.get())
            chain = self.Sel_Chain(self.interface_content)
            resi = self.Sel_Resi(self.interface_content)
            resn = self.Sel_Resn(self.interface_content)
            # print chain
            # print resi
            # print resn

            cmd.select("surf", resn + ' and ' + resi + ' and ' + chain)
            # cmd.color(self.surf_col,'surf')
        else:
            print ('NO Path Input')

    def execute(self, e_cmd):
        """ Run the cmd represented by the button clicked by user.
        """

        if e_cmd == 'Show interface h-bonds':
            self.show_hbonds_but()

        elif e_cmd== 'Hide nucleic':
            print('Hide ...')
            cmd.select('nucleic', 'resn DA+DC+DG+DT+DU+A+T+G+C+I+U+5IU')

            cmd.hide('everything', 'nucleic')
            # print ("Hide DNA or RNA")
            ####d Display
        elif e_cmd == 'Show nucleic':
            cmd.select('nucleic', 'resn DA+DC+DG+DT+DU+A+T+G+C+I+U+5IU')
            cmd.show('sphere', 'nucleic')
            # print ("Show DNA or RNA")

        elif e_cmd == 'Show HOH':
            cmd.select('HOH','resn HOH')
            cmd.show('sphere', 'HOH')

        elif e_cmd == 'Hide HOH':
            cmd.select('HOH','resn HOH')
            cmd.hide('everything', 'HOH')

        elif cmd == 'Exit':
            print('Exiting Plugin ...')
            if __name__ == '__main__':
                self.parent.destroy()
            else:
                cmd.delete("*")
                self.dialog.withdraw()

                print('Done.')


        else:
            self.dialog.withdraw()


# test


if __name__ == '__main__':
    class App:
        def my_show(self, *args, **kwargs):
            pass


    app = App()
    app.root = Tkinter.Tk()
    Pmw.initialise(app.root)
    app.root.title('It seems to work!')

    widget = start(app)
    app.root.mainloop()