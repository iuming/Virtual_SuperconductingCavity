TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build an IOC support library
LIBRARY_IOC += virtual_srfSupport

# Compile and add code to the support library
#virtual_srfSupport_SRCS += xxxRecord.c
#virtual_srfSupport_SRCS += devXxxSoft.c

# Link locally-provided code into the support library,
# rather than directly into the IOC application.
# This is required for dbdExpand to create a .dbd file that
# includes these definitions
#virtual_srfSupport_SRCS += dbSubExample.c
#virtual_srfSupport_SRCS += devVirtual_SRFVersion.c
#virtual_srfSupport_SRCS += Virtual_SRFFlag.c
#virtual_srfSupport_SRCS += initTrace.c

# Build the IOC application
PROD_IOC = Virtual_SRF

# Virtual_SRF.dbd will be created and installed
DBD += Virtual_SRF.dbd

# Virtual_SRF.dbd will include these files
Virtual_SRF_DBD += base.dbd
#Virtual_SRF_DBD += xxxSupport.dbd
#Virtual_SRF_DBD += dbSubExample.dbd
#Virtual_SRF_DBD += Virtual_SRFHello.dbd
#Virtual_SRF_DBD += initTrace.dbd

# Virtual_SRF_registerRecordDeviceDriver.cpp derives from Virtual_SRF.dbd
Virtual_SRF_SRCS += Virtual_SRF_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
Virtual_SRF_SRCS_DEFAULT += Virtual_SRFMain.cpp
Virtual_SRF_SRCS_vxWorks += -nil-

# Link in the code from our support library
Virtual_SRF_LIBS += virtual_srfSupport
Virtual_SRF_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
Virtual_SRF_LIBS += $(EPICS_BASE_LIBS)

#----------------------------------------
#  ADD RULES AFTER THIS LINE

include $(TOP)/configure/RULES