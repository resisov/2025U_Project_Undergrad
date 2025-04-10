# 2025U_Project_Undergrad

In your home directory, follow this command
```
source cmsset.sh
cd CMSSW_11_3_4/src
cmsenv
cd
```

Launch mg5
```
cd MG5_aMC_v3_5_8
./bin/mg5_aMC
```

This is a mg5 command
```
import model DMsimp_s_spin1
generate p p > t t~ xd xd~
output SMS_spin1_TTxdxdToInclusiveDecay_madgraph5_madspin
launch
```

Set like this
```
/=================== Description ===================|============= values ==============|======== other options ========\
| 1. Choose the shower/hadronization program        |        shower = OFF               |     Pythia8                   |
| 2. Choose the detector simulation program         |      detector = Not Avail.        |     Please install module     |
| 3. Choose an analysis package (plot/convert)      |      analysis = OFF               |     ExRoot                    |
| 4. Decay onshell particles                        |       madspin = onshell           |     full|OFF|ON               |
| 5. Add weights to events for new hypp.            |      reweight = OFF               |     ON                        |
\=======================================================================================================================/
```
press ```0``` and enter.

And press ```1``` to set a mediator mass.

You can change the mediator mass from ```5000001 1.000000e+03 # MY1 ``` to ```5000001 1.000000e+02 # MY1 ```

And please change the decay width from  ```DECAY 5000001 1.000000e+01 # WY1 ``` to ```DECAY 5000001 auto # WY1 ```

Save the setting ```:wq```
