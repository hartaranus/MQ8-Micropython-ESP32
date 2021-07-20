# MQ8-Micropython-ESP32
MQ-8 Hydrogen gas sensor module for micropython. This module has been tested on ESP-32

## Hardware Information
This module can be used without adding 1.47 kohm resistor to GPIO Pin
The default pin used was GPIO36 which labeled as VP on ESP32 board
Modify the code in MQ8.get_resistance() method to change the default Pin

## Circuit Wiring
Here's the connection setup
---------------------------
|   MQ8 To ESP32 Wiring   |
| ----------------------- |
| Sensor | ESP-32 | Label |
| VCC | 5V | Vin |
| GND | GND | GND |
| A0 | GPIO36 | VP |


## Additional Information
This software module is a part of Hydrogen Energy research in Wardana Research Group, Dept. of Mechanical Engineering, Universitas Brawijaya, Malang,Indonesia
This module is freely available for any kind of project in research scale, Minimum Viable Product design, Prototyping, and H2 gas detection
For Industrial Scale Hydrogen Production the use of this module and MQ-X sensor series is not recommended

## Responsible Person
Head of Wardana Research Group : Prof. ING. Wardana,Ph.D
Software Author                : Dr. WIlly Satrio N
Research Manager               : Dr. Purnami

## Contact Info
For Research Collaboration or Project please email to wardana@ub.ac.id and alternative contact to willy13101307@gmail.com

## Addresses
Universitas Brawijaya          : https://ub.ac.id/
Physical Address               : Jl. Veteran, Ketawanggede, Kec. Lowokwaru, Kota Malang, Jawa Timur 65145
Departement                    : Mechanical Engineering

## Terms and Conditions
If this module is usefull for your research project please cite one of scientific article listed below:
1. Hydrogen production from instant noodle wastewater by organic electrocatalyst coated on PVC surface 
   (https://doi.org/10.1016/j.ijhydene.2020.03.002)
2. Strengthening external magnetic fields with activated carbon graphene for increasing hydrogen production in water electrolysis 
   (https://doi.org/10.1016/j.ijhydene.2020.05.148)
3. The role of turmeric and bicnat on hydrogen production in porous tofu waste suspension electrolysis
   (https://doi.org/10.1007/s13399-020-00803-0)
4. Synergistic effect of curcumin and activated carbon catalyst enhancing hydrogen production from biomass pyrolysis
   (https://doi.org/10.1016/j.ijhydene.2020.11.211)
5. The role of activated carbon in boosting the activity of clitoria ternatea powder photocatalyst for hydrogen production
   (https://doi.org/10.1016/j.ijhydene.2020.05.103)
6. The effect of curcumin coated electrode on hydrogen production through water electrolysis
   (https://doi.org/10.1051/e3sconf/202018101003)
7. Hydrogen production by photocatalysis method of glutamic acid and activated carbon
   (https://doi.org/10.1051/e3sconf/202018101009)
8. Development Of Bamboo Charcoal And Fragaria Vesca Powder Photocatalysts In Hydrogen Production Via Water Splitting
   (DOI : 10.15587/1729-4061.2020.213277)


