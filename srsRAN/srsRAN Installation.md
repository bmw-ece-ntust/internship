## Installation

In order to download and build the srsRAN, there are four steps that need to be done:

1. Install Dependencies
2. Install RF Driver
3. Clone the Repository
4. Build the Codebase


### Install Dependencies
Input 

```
sudo apt-get install cmake make gcc g++ pkg-config libfftw3-dev libmbedtls-dev libsctp-dev libyaml-cpp-dev libgtest-dev
```

Output (First and Last 10 Lines)

```
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  bzip2 cmake-data cpp cpp-11 dh-elpa-helper emacsen-common fontconfig-config fonts-dejavu-core g++-11 gcc-11
  gcc-11-base googletest libarchive13 libasan6 libatomic1 libc-dev-bin libc-devtools libc6 libc6-dev libcc1-0
  libcrypt-dev libdeflate0 libdpkg-perl libfftw3-bin libfftw3-double3 libfftw3-long3 libfftw3-quad3
  libfile-fcntllock-perl libfontconfig1 libfreetype6 libgcc-11-dev libgd3 libisl23 libitm1 libjbig0 libjpeg-turbo8
  libjpeg8 libjsoncpp25 liblsan0 libmbedtls14 libmbedx509-1 libmpc3 libnsl-dev libquadmath0 librhash0 libstdc++-11-dev
  libtiff5 libtirpc-dev libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev manpages-dev rpcsvc-proto
Suggested packages:
.
.
.
Setting up libsctp-dev:amd64 (1.0.19+dfsg-1build1) ...
Setting up libstdc++-11-dev:amd64 (11.4.0-1ubuntu1~22.04) ...
Setting up libfftw3-dev:amd64 (3.3.8-2ubuntu8) ...
Setting up libc-devtools (2.35-0ubuntu3.6) ...
Setting up g++-11 (11.4.0-1ubuntu1~22.04) ...
Setting up g++ (4:11.2.0-1ubuntu1) ...
update-alternatives: using /usr/bin/g++ to provide /usr/bin/c++ (c++) in auto mode
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.1) ...
/sbin/ldconfig.real: /usr/lib/wsl/lib/libcuda.so.1 is not a symbolic link
```

### Install RF-Drivers


The srsRAN Project uses RF drivers to support different radio types.
Currently, only UHD is supported however additional drivers are under development


Input

```sudo apt-get install libuhd-dev uhd-host```

Output (First and Last 10 Lines)

```Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  adwaita-icon-theme alsa-topology-conf alsa-ucm-conf aspell aspell-en at-spi2-core bladerf blt bubblewrap castxml
  catch2 dbus-user-session dconf-gsettings-backend dconf-service desktop-file-utils dictionaries-common docbook-xml
  enchant-2 fdisk fontconfig fonts-lyx fonts-mathjax freeglut3 gdisk glib-networking glib-networking-common
  glib-networking-services gnome-terminal gnome-terminal-data gnuradio gnuradio-dev gsettings-desktop-schemas
  gstreamer1.0-gl gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-x gtk-update-icon-cache gvfs
  gvfs-common gvfs-daemons gvfs-libs hicolor-icon-theme humanity-icon-theme hunspell-en-us icu-devtools
.
.
.
aspell-autobuildhash: processing: en [en_GB-ize-w_accents-only].
aspell-autobuildhash: processing: en [en_GB-ize-wo_accents-only].
aspell-autobuildhash: processing: en [en_GB-variant_0].
aspell-autobuildhash: processing: en [en_GB-variant_1].
aspell-autobuildhash: processing: en [en_US-w_accents-only].
aspell-autobuildhash: processing: en [en_US-wo_accents-only].
Processing triggers for libgdk-pixbuf-2.0-0:amd64 (2.42.8+dfsg-1ubuntu0.2) ...
Processing triggers for libc-bin (2.35-0ubuntu3.1) ...
/sbin/ldconfig.real: /usr/lib/wsl/lib/libcuda.so.1 is not a symbolic link

Processing triggers for sgml-base (1.30) ...
```

### Clone the Repository


The link of the clone target is repository is https://github.com/srsRAN/srsRAN_Project.git


Input
```
git clone https://github.com/srsRAN/srsRAN_Project.git
```

Output
```
Cloning into 'srsRAN_Project'...
remote: Enumerating objects: 154279, done.
remote: Counting objects: 100% (27641/27641), done.
remote: Compressing objects: 100% (7606/7606), done.
remote: Total 154279 (delta 20321), reused 25878 (delta 19587), pack-reused 126638
Receiving objects: 100% (154279/154279), 48.35 MiB | 3.66 MiB/s, done.
Resolving deltas: 100% (120877/120877), done.
```

### Build the Codebase

Input
```
cd srsRAN_Project
mkdir build
cd build
cmake ../
make -j $(nproc)
make test -j $(nproc)
```
Output (cmake ../)
```
-- The C compiler identification is GNU 11.4.0
-- The CXX compiler identification is GNU 11.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Build type not specified: defaulting to Release.
-- Performing Test HAS_MAYBE_UNINITIALIZED
-- Performing Test HAS_MAYBE_UNINITIALIZED - Success
-- Performing Test HAVE_NON_VIRTUAL_DTOR
-- Performing Test HAVE_NON_VIRTUAL_DTOR - Success
-- Performing Test HAVE_SUGGEST_OVERRIDE
-- Performing Test HAVE_SUGGEST_OVERRIDE - Success
-- Performing Test HAVE_SHADOW
-- Performing Test HAVE_SHADOW - Success
-- Assertion level set to NORMAL
-- Could NOT find libdw (missing: LIBDW_LIBRARY LIBDW_INCLUDE_DIR)
-- Could NOT find libbfd (missing: LIBBFD_LIBRARY LIBBFD_INCLUDE_DIR)
-- Could NOT find libdwarf (missing: LIBDWARF_LIBRARY LIBDWARF_INCLUDE_DIR LIBELF_LIBRARY LIBELF_INCLUDE_DIR)
-- Found Backward: /home/arrifqi/srsRAN_Project/cmake/modules
-- Backward-cpp found, but external libraries are missing.
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.2")
-- Checking for module 'mbedtls'
--   No package 'mbedtls' found
-- MBEDTLS LIBRARIES: /usr/lib/x86_64-linux-gnu/libmbedcrypto.so
-- MBEDTLS STATIC LIBRARIES: /usr/lib/x86_64-linux-gnu/libmbedcrypto.a
-- MBEDTLS INCLUDE DIRS: /usr/include
-- Found MbedTLS: /usr/lib/x86_64-linux-gnu/libmbedcrypto.so
-- Checking for module 'fftw3f >= 3.0'
--   Found fftw3f , version 3.3.8
-- FFTW3F LIBRARIES: /usr/lib/x86_64-linux-gnu/libfftw3f.so
-- FFTW3F STATIC LIBRARIES: /usr/lib/x86_64-linux-gnu/libfftw3f.a
-- FFTW3F INCLUDE DIRS: /usr/include
-- Found FFTW3F: /usr/lib/x86_64-linux-gnu/libfftw3f.so
-- Found GTest: /usr/lib/x86_64-linux-gnu/cmake/GTest/GTestConfig.cmake (found version "1.11.0")
-- Found Threads: TRUE
-- UHD LIBRARIES /usr/lib/x86_64-linux-gnu/libuhd.so
-- UHD INCLUDE DIRS /usr/include
-- Found UHD: /usr/lib/x86_64-linux-gnu/libuhd.so
-- Checking for module 'yaml-cpp'
--   Found yaml-cpp, version 0.7.0
-- YAMLCPP LIBRARIES: /usr/lib/x86_64-linux-gnu/libyaml-cpp.so
-- YAMLCPP INCLUDE DIRS: /usr/include
-- Found YAMLCPP: /usr/lib/x86_64-linux-gnu/libyaml-cpp.so
-- Performing Test HAVE_SSE
-- Performing Test HAVE_SSE - Success
-- SSE4.1 is enabled - target CPU must support it
-- Performing Test HAVE_AVX
-- Performing Test HAVE_AVX - Success
-- AVX is enabled - target CPU must support it
-- Performing Test HAVE_AVX2
-- Performing Test HAVE_AVX2 - Success
-- AVX2 is enabled - target CPU must support it
-- Performing Test HAVE_FMA
-- Performing Test HAVE_FMA - Success
-- FMA is enabled - target CPU must support it
-- Performing Test HAVE_AVX512
-- Performing Test HAVE_AVX512 - Failed
-- Performing Test HAVE_MARCH
-- Performing Test HAVE_MARCH - Success
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE)
-- Checking for module 'sctp'
--   No package 'sctp' found
-- SCTP LIBRARIES: /usr/lib/x86_64-linux-gnu/libsctp.so
-- SCTP INCLUDE DIRS: /usr/include
-- Found SCTP: /usr/lib/x86_64-linux-gnu/libsctp.so
-- FFT_LIBRARIES: /usr/lib/x86_64-linux-gnu/libfftw3f.so
-- Building srsRAN version 23.10.1
-- Configuring done
-- Generating done
-- Build files have been written to: /home/arrifqi/srsRAN_Project/build
```

Output (first and last 10 lines of make -j $(nproc))
```
[  0%] Building CXX object lib/scheduler/cell/CMakeFiles/sched_cell.dir/vrb_alloc.cpp.o
[  0%] Building CXX object external/fmt/CMakeFiles/fmt.dir/src/format.cc.o
[  0%] Building CXX object lib/scheduler/cell/CMakeFiles/sched_cell.dir/resource_block_group.cpp.o
[  0%] Building CXX object lib/scheduler/ue_scheduling/CMakeFiles/ue_sched.dir/harq_process.cpp.o
[  0%] Building CXX object external/fmt/CMakeFiles/fmt.dir/src/os.cc.o
[  0%] Building CXX object lib/scheduler/cell/CMakeFiles/sched_cell.dir/scheduler_prb.cpp.o
[  0%] Building CXX object lib/pcap/CMakeFiles/srsran_pcap.dir/backend_pcap_writer.cpp.o
[  0%] Building CXX object lib/du/CMakeFiles/srsran_du_config_validators.dir/du_cell_config_validation.cpp.o
[  0%] Building CXX object lib/scheduler/cell/CMakeFiles/sched_cell.dir/resource_grid.cpp.o
[  0%] Building CXX object lib/du_manager/du_ue/CMakeFiles/du_ue.dir/du_bearer.cpp.o
.
.
.
[100%] Built target du_example
[100%] Built target cu_du_test
[100%] Linking CXX executable du_high_benchmark
[100%] Built target du_high_benchmark
[100%] Linking CXX executable du_high_test
[100%] Linking CXX executable paging_du_high_test
[100%] Built target du_high_test
[100%] Built target paging_du_high_test
[100%] Linking CXX executable gnb
[100%] Built target gnb
```

Output (Tail of make test -j $(nproc))
```
100% tests passed, 0 tests failed out of 4524

Label Time Summary:
adt                  =   1.59 sec*proc (358 tests)
asn1                 =   0.29 sec*proc (30 tests)
cell_meas_manager    =   0.04 sec*proc (11 tests)
cu                   =   0.03 sec*proc (1 test)
cu_cp                =   1.10 sec*proc (111 tests)
cu_cp_ue_manager     =   0.09 sec*proc (17 tests)
cu_up                =   0.09 sec*proc (15 tests)
cu_up_processor      =   0.01 sec*proc (1 test)
du                   =   0.03 sec*proc (1 test)
du_high              =   2.58 sec*proc (3 tests)
du_high|tsan         =   0.15 sec*proc (1 test)
du_manager           =   0.63 sec*proc (108 tests)
du_processor         =   0.45 sec*proc (38 tests)
e1ap                 =   0.22 sec*proc (33 tests)
e1ap_cu_cp           =   0.13 sec*proc (21 tests)
e1ap_cu_up           =   0.07 sec*proc (10 tests)
e2ap                 =   2.25 sec*proc (23 tests)
ecpri                =   0.02 sec*proc (8 tests)
ethernet             =   1.79 sec*proc (99 tests)
f1ap                 =   0.54 sec*proc (62 tests)
f1ap_cu              =   0.22 sec*proc (29 tests)
f1ap_du              =   0.28 sec*proc (25 tests)
fapi                 =   2.63 sec*proc (1586 tests)
fapi_adaptor         =   0.28 sec*proc (52 tests)
gateways             =   4.00 sec*proc (19 tests)
gtpu                 =   0.16 sec*proc (23 tests)
integrationtest      =   2.62 sec*proc (4 tests)
io_broker            =   3.79 sec*proc (9 tests)
mac                  =   0.44 sec*proc (55 tests)
mobility             =   0.11 sec*proc (6 tests)
ngap                 =   0.34 sec*proc (40 tests)
ofh                  =   0.01 sec*proc (7 tests)
pcap                 =   0.22 sec*proc (11 tests)
pdcp                 =   5.25 sec*proc (152 tests)
phy                  =   3.84 sec*proc (114 tests)
psup                 =   0.05 sec*proc (6 tests)
ran                  =   1.09 sec*proc (309 tests)
receiver             =   0.25 sec*proc (88 tests)
rlc                  =   1.70 sec*proc (175 tests)
rrc                  =   0.14 sec*proc (15 tests)
rrc_ue               =   0.14 sec*proc (15 tests)
sched                =   8.52 sec*proc (796 tests)
security             =   0.33 sec*proc (46 tests)
serdes               =   0.12 sec*proc (46 tests)
support              =   0.26 sec*proc (32 tests)
transmitter          =   0.46 sec*proc (29 tests)
tsan                 =   3.12 sec*proc (14 tests)
vectortest           =   0.02 sec*proc (4 tests)

Total Test time (real) =  49.09 sec
```

### Install the srsRAN Project gNB

Input
```
sudo make install
```

Output (Head and Tail)
```
[  1%] Built target fmt
[  1%] Built target srslog
[  1%] Built target srsran_network
[  2%] Built target srsran_support
[  2%] Built target asn1_utils
[  3%] Built target rrc_nr_asn1
[  3%] Built target f1ap_asn1
[  3%] Built target e2ap_asn1
[  3%] Built target srsran_du_config_validators
[  5%] Built target srsran_ran
[  6%] Built target mac_configuration_helpers
[  6%] Built target sched_config_manager
[  7%] Built target scheduler_logger
[  7%] Built target sched_cell
[  8%] Built target common_sched
[  9%] Built target ue_sched
[ 10%] Built target sched_config
.
.
.
[100%] Built target pdcp_rx_benchmark
Install the project...
-- Install configuration: "Release"
-- Installing: /usr/local/bin/gnb
-- Set runtime path of "/usr/local/bin/gnb" to ""
-- Installing: /usr/local/share/srsran/geo_ntn.yml
-- Installing: /usr/local/share/srsran/gnb_custom_cell_properties.yml
-- Installing: /usr/local/share/srsran/gnb_rf_b200_tdd_n78_20mhz.yml
-- Installing: /usr/local/share/srsran/gnb_rf_b210_fdd_srsUE.yml
-- Installing: /usr/local/share/srsran/gnb_rf_n310_fdd_n3_20mhz.yml
-- Installing: /usr/local/share/srsran/gnb_ru_picocom_scb_tdd_n78_20mhz.yml
-- Installing: /usr/local/share/srsran/gnb_ru_ran550_tdd_n78_100mhz_2x2.yml
-- Installing: /usr/local/share/srsran/gnb_ru_ran550_tdd_n78_20mhz.yml
-- Installing: /usr/local/share/srsran/gnb_ru_rpqn4800e_tdd_n78_20mhz.yml
-- Installing: /usr/local/share/srsran/mimo_usrp.yml
-- Installing: /usr/local/share/srsran/mobility.yml
-- Installing: /usr/local/share/srsran/qam256.yml
-- Installing: /usr/local/share/srsran/qos.yml
-- Installing: /usr/local/share/srsran/slicing.yml
-- Installing: /usr/local/share/srsran/srb.yml
-- Installing: /usr/local/lib/libfmt.a
-- Installing: /usr/local/lib/libsrsran_instrumentation.a
-- Installing: /usr/local/lib/libsrsran_channel_precoder.a
-- Installing: /usr/local/lib/libsrsran_generic_funcs.a
-- Installing: /usr/local/lib/libsrsran_generic_funcs_dft.a
-- Installing: /usr/local/lib/libsrsran_phy_support.a
-- Installing: /usr/local/lib/libsrsran_channel_coding.a
-- Installing: /usr/local/lib/libsrsran_crc_calculator.a
-- Installing: /usr/local/lib/libsrsran_polar.a
-- Installing: /usr/local/lib/libsrsran_ldpc.a
-- Installing: /usr/local/lib/libsrsran_short_block.a
-- Installing: /usr/local/lib/libsrsran_channel_modulation.a
-- Installing: /usr/local/lib/libsrsran_channel_processors.a
-- Installing: /usr/local/lib/libsrsran_pbch_encoder.a
-- Installing: /usr/local/lib/libsrsran_pbch_modulator.a
-- Installing: /usr/local/lib/libsrsran_pdcch_encoder.a
-- Installing: /usr/local/lib/libsrsran_pdcch_modulator.a
-- Installing: /usr/local/lib/libsrsran_pdcch_processor.a
-- Installing: /usr/local/lib/libsrsran_pdsch_encoder.a
-- Installing: /usr/local/lib/libsrsran_pdsch_modulator.a
-- Installing: /usr/local/lib/libsrsran_pdsch_processor.a
-- Installing: /usr/local/lib/libsrsran_prach_detector.a
-- Installing: /usr/local/lib/libsrsran_pucch_demodulator.a
-- Installing: /usr/local/lib/libsrsran_pucch_detector.a
-- Installing: /usr/local/lib/libsrsran_pucch_processor.a
-- Installing: /usr/local/lib/libsrsran_pusch_processor.a
-- Installing: /usr/local/lib/libsrsran_ssb_processor.a
-- Installing: /usr/local/lib/libsrsran_uci_decoder.a
-- Installing: /usr/local/lib/libsrsran_channel_equalizer.a
-- Installing: /usr/local/lib/libsrsran_sequence_generators.a
-- Installing: /usr/local/lib/libsrsran_signal_processors.a
-- Installing: /usr/local/lib/liblog_likelihood_ratio.a
-- Installing: /usr/local/lib/libsrsran_upper_phy_support.a
-- Installing: /usr/local/lib/libsrsran_radio_uhd.a
-- Installing: /usr/local/lib/libsrsran_radio.a
-- Installing: /usr/local/lib/libsrsran_ran.a
-- Installing: /usr/local/lib/libsrslog.a
-- Installing: /usr/local/lib/libsrsvec.a
-- Installing: /usr/local/lib/libsrsran_network.a
-- Installing: /usr/local/lib/libsrsran_support.a
```

## Source
* https://docs.srsran.com/projects/project/en/latest/user_manuals/source/installation.html
* https://files.ettus.com/manual/page_install.html
