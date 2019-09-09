# InPrNa

This work was supported by Natural Science Foundation of Henan province (182300410368, 182300410130, 182300410306, 162300410177), the Production and Learning Cooperation and Cooperative Education Project of Ministry of Education of China (201702115008), National Natural Science Foundation of China (No. 61772176,61402153), the Science and Technology Research Key Project of Educational Department of Henan Province (No. 16A520016, 17B520002, 17B520036), Key Project of Science and Technology Department of Henan Province (No. 182102210208, 142102210056, 17B520002), Ph.D. Research Startup Foundation of Henan Normal University (Nos.qd15130, qd15132, qd15129), China Postdoctoral Science Foundation (No. 2016M602247), the Young Scholar Program of Henan Province (2017GGJS041), and the Key Scientific and Technological Project of Xinxiang City Of China (No. CXGG17002).

## Installation
Open Pymol, click on the Plguin option in the menu bar and select Plguin Manager. In the pop-up window, select Install New plugin and select the InPrNa.py file to install.

## Import PDB
Open InPrNa in pymol, click the Browse button to select the pdb file, and then click the load PDB button to import the PDB file. The import process may take a few minutes to calculate the interface information.

## Main interface
### Setting Interface Information
In the main interface of the Visualization tab, in the interface setting box, set the color of the interface part, display mode, and the Euclidian Distance of interface. After clicking the “APPLY" button, the residue binding sites will be displayed on the Pymol main interface, and the plugin window will also pop up.

At the same time, the information of amino acid components of the interface will be displayed in the box below the plugin.

The color and display mode of proteins and nucleic acids can also be set under the Visualization tab of the main interface.

At the bottom of the plugin, user can click on the button to choose to display hidden nucleic acids and proteins.
Properties Setting interface

Under the Amino acid tab of the main interface, select the physicochemical properties and set its color. after user clicked the APPLY button, user can observe the distribution of all residues in the protein with this physicochemical property in Pymol.

At the same time, the amount information of the residues having such physicochemical properties will be displayed in the lower part of the plugin

## Bump setting
We divide the spatial structure of the protein into three types: peak, flat, valley.

Under the Bump tab of the InPrNa interface, user can set the color and display mode of these three forms.
Users can also choose this three forms display areas , and user can choose whether the entire protein or the interface of different Euclidean distances.


