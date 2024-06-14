#!../../bin/windows-x64/Virtual_SRF

## You may have to change Virtual_SRF to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/Virtual_SRF.dbd"
Virtual_SRF_registerRecordDeviceDriver pdbbase

# Load record instances
dbLoadRecords "db/Cavity.db", "user=Virtual_SRF"
dbLoadRecords "db/PowerSource.db", "user=Virtual_SRF"
dbLoadRecords "db/FPC.db", "user=Virtual_SRF"
dbLoadRecords "db/Tuner.db", "user=Virtual_SRF"
dbLoadRecords "db/Cryogen.db", "user=Virtual_SRF"

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncExample, "user=Virtual_SRF"