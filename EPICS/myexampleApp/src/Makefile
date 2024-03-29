TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Use typed rset structure (see 3.16.1 release notes)
USR_CPPFLAGS += -DUSE_TYPED_RSET

# xxxRecord.h will be created from xxxRecord.dbd
DBDINC += xxxRecord

# Install xxxSupport.dbd into <top>/dbd
DBD += xxxSupport.dbd

# Build an IOC support library
LIBRARY_IOC += myexampleSupport

# Compile and add code to the support library
myexampleSupport_SRCS += xxxRecord.c
myexampleSupport_SRCS += devXxxSoft.c

# Link locally-provided code into the support library,
# rather than directly into the IOC application, that
# causes problems on Windows DLL builds
myexampleSupport_SRCS += dbSubExample.c
myexampleSupport_SRCS += devmyexampleVersion.c
myexampleSupport_SRCS += myexampleHello.c
myexampleSupport_SRCS += initTrace.c

myexampleSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Auto-generate a header file containing a version string.
# Version comes from the VCS if available, else date+time.
GENVERSION = myexampleVersion.h
# Macro name
GENVERSIONMACRO = myexampleVERSION

# Build the IOC application
PROD_IOC = myexample

# myexample.dbd will be created and installed
DBD += myexample.dbd

# myexample.dbd will include these files:
myexample_DBD += base.dbd
myexample_DBD += xxxSupport.dbd
myexample_DBD += dbSubExample.dbd
myexample_DBD += devmyexampleVersion.dbd
myexample_DBD += myexampleHello.dbd
myexample_DBD += initTrace.dbd

# myexample_registerRecordDeviceDriver.cpp derives from myexample.dbd
myexample_SRCS += myexample_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
myexample_SRCS_DEFAULT += myexampleMain.cpp
myexample_SRCS_vxWorks += -nil-

# Link in the code from our support library
myexample_LIBS += myexampleSupport

# To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
    # Build sncExample into myexampleSupport
    sncExample_SNCFLAGS += +r
    myexample_DBD += sncExample.dbd
    # A .stt sequence program is *not* pre-processed:
    myexampleSupport_SRCS += sncExample.stt
    myexampleSupport_LIBS += seq pv
    myexample_LIBS += seq pv

    # Build sncProgram as a standalone program
    PROD_HOST += sncProgram
    sncProgram_SNCFLAGS += +m
    # A .st sequence program *is* pre-processed:
    sncProgram_SRCS += sncProgram.st
    sncProgram_LIBS += seq pv
    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
endif

# Link QSRV (pvAccess Server) if available
ifdef EPICS_QSRV_MAJOR_VERSION
    myexample_LIBS += qsrv
    myexample_LIBS += $(EPICS_BASE_PVA_CORE_LIBS)
    myexample_DBD += PVAServerRegister.dbd
    myexample_DBD += qsrv.dbd
endif

# Finally link IOC to the EPICS Base libraries
myexample_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

# Explicit dependency needed for generated header file
devmyexampleVersion$(DEP): $(COMMON_DIR)/$(GENVERSION)
