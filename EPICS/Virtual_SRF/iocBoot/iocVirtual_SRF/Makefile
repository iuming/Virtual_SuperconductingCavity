# Makefile for iocBoot/iocVirtual_SRF

PROD_IOC = Virtual_SRF
DBD = $(PROD_IOC).dbd

# Virtual_SRF.dbd will be created and installed
DBD += Virtual_SRF.dbd

# Virtual_SRF.dbd will include these files
Virtual_SRF_DBD += base.dbd

# Virtual_SRF_registerRecordDeviceDriver.cpp derives from Virtual_SRF.dbd
Virtual_SRF_SRCS += Virtual_SRF_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
Virtual_SRF_SRCS_DEFAULT += Virtual_SRFMain.cpp
Virtual_SRF_SRCS_vxWorks += -nil-

# Link in the code from our support library
Virtual_SRF_LIBS += virtual_srfSupport

# Finally link IOC to the EPICS Base libraries
Virtual_SRF_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES