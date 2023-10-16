from __future__ import annotations
from typing import overload, Any, List, Dict, Tuple, Set, Sequence, Union
from pyopenms import *  # pylint: disable=wildcard-import; lgtm(py/polluting-import)
import numpy as _np

from enum import Enum as _PyEnum


def __static_File_absolutePath(file: Union[bytes, str, String] ) -> Union[bytes, str, String]:
    """
    Cython signature: String absolutePath(String file)
    """
    ...

def __static_File_basename(file: Union[bytes, str, String] ) -> Union[bytes, str, String]:
    """
    Cython signature: String basename(String file)
    """
    ...

def __static_PrecursorCorrection_correctToHighestIntensityMS1Peak(exp: MSExperiment , mz_tolerance: float , ppm: bool , delta_mzs: List[float] , mzs: List[float] , rts: List[float] ) -> Set[int]:
    """
    Cython signature: libcpp_set[size_t] correctToHighestIntensityMS1Peak(MSExperiment & exp, double mz_tolerance, bool ppm, libcpp_vector[double] & delta_mzs, libcpp_vector[double] & mzs, libcpp_vector[double] & rts)
    """
    ...

def __static_PrecursorCorrection_correctToNearestFeature(features: FeatureMap , exp: MSExperiment , rt_tolerance_s: float , mz_tolerance: float , ppm: bool , believe_charge: bool , keep_original: bool , all_matching_features: bool , max_trace: int , debug_level: int ) -> Set[int]:
    """
    Cython signature: libcpp_set[size_t] correctToNearestFeature(FeatureMap & features, MSExperiment & exp, double rt_tolerance_s, double mz_tolerance, bool ppm, bool believe_charge, bool keep_original, bool all_matching_features, int max_trace, int debug_level)
    """
    ...

def __static_PrecursorCorrection_correctToNearestMS1Peak(exp: MSExperiment , mz_tolerance: float , ppm: bool , delta_mzs: List[float] , mzs: List[float] , rts: List[float] ) -> Set[int]:
    """
    Cython signature: libcpp_set[size_t] correctToNearestMS1Peak(MSExperiment & exp, double mz_tolerance, bool ppm, libcpp_vector[double] & delta_mzs, libcpp_vector[double] & mzs, libcpp_vector[double] & rts)
    """
    ...

def __static_Deisotoper_deisotopeAndSingleCharge(spectra: MSSpectrum , fragment_tolerance: float , fragment_unit_ppm: bool , min_charge: int , max_charge: int , keep_only_deisotoped: bool , min_isopeaks: int , max_isopeaks: int , make_single_charged: bool , annotate_charge: bool , annotate_iso_peak_count: bool , use_decreasing_model: bool , start_intensity_check: int , add_up_intensity: bool ) -> None:
    """
    Cython signature: void deisotopeAndSingleCharge(MSSpectrum & spectra, double fragment_tolerance, bool fragment_unit_ppm, int min_charge, int max_charge, bool keep_only_deisotoped, unsigned int min_isopeaks, unsigned int max_isopeaks, bool make_single_charged, bool annotate_charge, bool annotate_iso_peak_count, bool use_decreasing_model, unsigned int start_intensity_check, bool add_up_intensity)
    """
    ...

def __static_Deisotoper_deisotopeAndSingleChargeDefault(spectra: MSSpectrum , fragment_tolerance: float , fragment_unit_ppm: bool ) -> None:
    """
    Cython signature: void deisotopeAndSingleChargeDefault(MSSpectrum & spectra, double fragment_tolerance, bool fragment_unit_ppm)
    """
    ...

def __static_Deisotoper_deisotopeWithAveragineModel(spectrum: MSSpectrum , fragment_tolerance: float , fragment_unit_ppm: bool , number_of_final_peaks: int , min_charge: int , max_charge: int , keep_only_deisotoped: bool , min_isopeaks: int , max_isopeaks: int , make_single_charged: bool , annotate_charge: bool , annotate_iso_peak_count: bool , add_up_intensity: bool ) -> None:
    """
    Cython signature: void deisotopeWithAveragineModel(MSSpectrum & spectrum, double fragment_tolerance, bool fragment_unit_ppm, int number_of_final_peaks, int min_charge, int max_charge, bool keep_only_deisotoped, unsigned int min_isopeaks, unsigned int max_isopeaks, bool make_single_charged, bool annotate_charge, bool annotate_iso_peak_count, bool add_up_intensity)
    """
    ...

def __static_File_empty(file_: Union[bytes, str, String] ) -> bool:
    """
    Cython signature: bool empty(String file_)
    """
    ...

def __static_File_exists(file_: Union[bytes, str, String] ) -> bool:
    """
    Cython signature: bool exists(String file_)
    """
    ...

def __static_File_fileList(dir: Union[bytes, str, String] , file_pattern: Union[bytes, str, String] , output: List[bytes] , full_path: bool ) -> bool:
    """
    Cython signature: bool fileList(String dir, String file_pattern, StringList output, bool full_path)
    """
    ...

def __static_File_find(filename: Union[bytes, str, String] , directories: List[bytes] ) -> Union[bytes, str, String]:
    """
    Cython signature: String find(String filename, StringList directories)
    """
    ...

def __static_File_findDatabase(db_name: Union[bytes, str, String] ) -> Union[bytes, str, String]:
    """
    Cython signature: String findDatabase(String db_name)
    """
    ...

def __static_File_findDoc(filename: Union[bytes, str, String] ) -> Union[bytes, str, String]:
    """
    Cython signature: String findDoc(String filename)
    """
    ...

def __static_File_findExecutable(toolName: Union[bytes, str, String] ) -> Union[bytes, str, String]:
    """
    Cython signature: String findExecutable(String toolName)
    """
    ...

def __static_File_getExecutablePath() -> Union[bytes, str, String]:
    """
    Cython signature: String getExecutablePath()
    """
    ...

def __static_File_getOpenMSDataPath() -> Union[bytes, str, String]:
    """
    Cython signature: String getOpenMSDataPath()
    """
    ...

def __static_File_getOpenMSHomePath() -> Union[bytes, str, String]:
    """
    Cython signature: String getOpenMSHomePath()
    """
    ...

def __static_PrecursorCorrection_getPrecursors(exp: MSExperiment , precursors: List[Precursor] , precursors_rt: List[float] , precursor_scan_index: List[int] ) -> None:
    """
    Cython signature: void getPrecursors(MSExperiment & exp, libcpp_vector[Precursor] & precursors, libcpp_vector[double] & precursors_rt, libcpp_vector[size_t] & precursor_scan_index)
    """
    ...

def __static_File_getSystemParameters() -> Param:
    """
    Cython signature: Param getSystemParameters()
    """
    ...

def __static_File_getTempDirectory() -> Union[bytes, str, String]:
    """
    Cython signature: String getTempDirectory()
    """
    ...

def __static_File_getTemporaryFile(alternative_file: Union[bytes, str, String] ) -> Union[bytes, str, String]:
    """
    Cython signature: String getTemporaryFile(const String & alternative_file)
    """
    ...

def __static_File_getUniqueName() -> Union[bytes, str, String]:
    """
    Cython signature: String getUniqueName()
    """
    ...

def __static_File_getUserDirectory() -> Union[bytes, str, String]:
    """
    Cython signature: String getUserDirectory()
    """
    ...

def __static_File_isDirectory(path: Union[bytes, str, String] ) -> bool:
    """
    Cython signature: bool isDirectory(String path)
    """
    ...

def __static_CachedmzML_load(filename: Union[bytes, str, String] , exp: CachedmzML ) -> None:
    """
    Cython signature: void load(const String & filename, CachedmzML & exp)
    """
    ...

def __static_File_path(file: Union[bytes, str, String] ) -> Union[bytes, str, String]:
    """
    Cython signature: String path(String file)
    """
    ...

def __static_File_readable(file: Union[bytes, str, String] ) -> bool:
    """
    Cython signature: bool readable(String file)
    """
    ...

def __static_File_remove(file_: Union[bytes, str, String] ) -> bool:
    """
    Cython signature: bool remove(String file_)
    """
    ...

def __static_File_removeDirRecursively(dir_name: Union[bytes, str, String] ) -> bool:
    """
    Cython signature: bool removeDirRecursively(String dir_name)
    """
    ...

def __static_File_rename(from_: Union[bytes, str, String] , to: Union[bytes, str, String] , overwrite_existing: bool , verbose: bool ) -> bool:
    """
    Cython signature: bool rename(const String & from_, const String & to, bool overwrite_existing, bool verbose)
    """
    ...

def __static_CachedmzML_store(filename: Union[bytes, str, String] , exp: MSExperiment ) -> None:
    """
    Cython signature: void store(const String & filename, MSExperiment exp)
    """
    ...

def __static_File_writable(file: Union[bytes, str, String] ) -> bool:
    """
    Cython signature: bool writable(String file)
    """
    ...

def __static_PrecursorCorrection_writeHist(out_csv: String , delta_mzs: List[float] , mzs: List[float] , rts: List[float] ) -> None:
    """
    Cython signature: void writeHist(String & out_csv, libcpp_vector[double] & delta_mzs, libcpp_vector[double] & mzs, libcpp_vector[double] & rts)
    """
    ...


class AccurateMassSearchResult:
    """
    Cython implementation of _AccurateMassSearchResult

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1AccurateMassSearchResult.html>`_
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void AccurateMassSearchResult()
        """
        ...
    
    def getObservedMZ(self) -> float:
        """
        Cython signature: double getObservedMZ()
        """
        ...
    
    def setObservedMZ(self, m: float ) -> None:
        """
        Cython signature: void setObservedMZ(double & m)
        """
        ...
    
    def getCalculatedMZ(self) -> float:
        """
        Cython signature: double getCalculatedMZ()
        """
        ...
    
    def setCalculatedMZ(self, m: float ) -> None:
        """
        Cython signature: void setCalculatedMZ(double & m)
        """
        ...
    
    def getQueryMass(self) -> float:
        """
        Cython signature: double getQueryMass()
        """
        ...
    
    def setQueryMass(self, m: float ) -> None:
        """
        Cython signature: void setQueryMass(double & m)
        """
        ...
    
    def getFoundMass(self) -> float:
        """
        Cython signature: double getFoundMass()
        """
        ...
    
    def setFoundMass(self, m: float ) -> None:
        """
        Cython signature: void setFoundMass(double & m)
        """
        ...
    
    def getCharge(self) -> float:
        """
        Cython signature: double getCharge()
        """
        ...
    
    def setCharge(self, ch: float ) -> None:
        """
        Cython signature: void setCharge(double & ch)
        """
        ...
    
    def getMZErrorPPM(self) -> float:
        """
        Cython signature: double getMZErrorPPM()
        """
        ...
    
    def setMZErrorPPM(self, ppm: float ) -> None:
        """
        Cython signature: void setMZErrorPPM(double & ppm)
        """
        ...
    
    def getObservedRT(self) -> float:
        """
        Cython signature: double getObservedRT()
        """
        ...
    
    def setObservedRT(self, rt: float ) -> None:
        """
        Cython signature: void setObservedRT(double & rt)
        """
        ...
    
    def getObservedIntensity(self) -> float:
        """
        Cython signature: double getObservedIntensity()
        """
        ...
    
    def setObservedIntensity(self, intensity: float ) -> None:
        """
        Cython signature: void setObservedIntensity(double & intensity)
        """
        ...
    
    def getMatchingIndex(self) -> float:
        """
        Cython signature: double getMatchingIndex()
        """
        ...
    
    def setMatchingIndex(self, idx: float ) -> None:
        """
        Cython signature: void setMatchingIndex(double & idx)
        """
        ...
    
    def getFoundAdduct(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getFoundAdduct()
        """
        ...
    
    def setFoundAdduct(self, add: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setFoundAdduct(const String & add)
        """
        ...
    
    def getFormulaString(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getFormulaString()
        """
        ...
    
    def setEmpiricalFormula(self, ep: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setEmpiricalFormula(const String & ep)
        """
        ...
    
    def getMatchingHMDBids(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getMatchingHMDBids()
        """
        ...
    
    def setMatchingHMDBids(self, match_ids: List[bytes] ) -> None:
        """
        Cython signature: void setMatchingHMDBids(libcpp_vector[String] & match_ids)
        """
        ...
    
    def getIsotopesSimScore(self) -> float:
        """
        Cython signature: double getIsotopesSimScore()
        """
        ...
    
    def setIsotopesSimScore(self, sim_score: float ) -> None:
        """
        Cython signature: void setIsotopesSimScore(double & sim_score)
        """
        ...
    
    def getIndividualIntensities(self) -> List[float]:
        """
        Cython signature: libcpp_vector[double] getIndividualIntensities()
        """
        ...
    
    def setIndividualIntensities(self, in_0: List[float] ) -> None:
        """
        Cython signature: void setIndividualIntensities(libcpp_vector[double])
        """
        ...
    
    def getSourceFeatureIndex(self) -> int:
        """
        Cython signature: size_t getSourceFeatureIndex()
        """
        ...
    
    def setSourceFeatureIndex(self, in_0: int ) -> None:
        """
        Cython signature: void setSourceFeatureIndex(size_t)
        """
        ...
    
    def getMasstraceIntensities(self) -> List[float]:
        """
        Cython signature: libcpp_vector[double] getMasstraceIntensities()
        """
        ...
    
    def setMasstraceIntensities(self, in_0: List[float] ) -> None:
        """
        Cython signature: void setMasstraceIntensities(libcpp_vector[double] &)
        """
        ... 


class Acquisition:
    """
    Cython implementation of _Acquisition

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1Acquisition.html>`_
      -- Inherits from ['MetaInfoInterface']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void Acquisition()
        """
        ...
    
    @overload
    def __init__(self, in_0: Acquisition ) -> None:
        """
        Cython signature: void Acquisition(Acquisition &)
        """
        ...
    
    def getIdentifier(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getIdentifier()
        """
        ...
    
    def setIdentifier(self, identifier: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setIdentifier(const String & identifier)
        """
        ...
    
    def isMetaEmpty(self) -> bool:
        """
        Cython signature: bool isMetaEmpty()
        Returns if the MetaInfo is empty
        """
        ...
    
    def clearMetaInfo(self) -> None:
        """
        Cython signature: void clearMetaInfo()
        Removes all meta values
        """
        ...
    
    def metaRegistry(self) -> MetaInfoRegistry:
        """
        Cython signature: MetaInfoRegistry metaRegistry()
        Returns a reference to the MetaInfoRegistry
        """
        ...
    
    def getKeys(self, keys: List[bytes] ) -> None:
        """
        Cython signature: void getKeys(libcpp_vector[String] & keys)
        Fills the given vector with a list of all keys for which a value is set
        """
        ...
    
    def getMetaValue(self, in_0: Union[bytes, str, String] ) -> Union[int, float, bytes, str, List[int], List[float], List[bytes]]:
        """
        Cython signature: DataValue getMetaValue(String)
        Returns the value corresponding to a string, or
        """
        ...
    
    def setMetaValue(self, in_0: Union[bytes, str, String] , in_1: Union[int, float, bytes, str, List[int], List[float], List[bytes]] ) -> None:
        """
        Cython signature: void setMetaValue(String, DataValue)
        Sets the DataValue corresponding to a name
        """
        ...
    
    def metaValueExists(self, in_0: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool metaValueExists(String)
        Returns whether an entry with the given name exists
        """
        ...
    
    def removeMetaValue(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void removeMetaValue(String)
        Removes the DataValue corresponding to `name` if it exists
        """
        ...
    
    def __richcmp__(self, other: Acquisition, op: int) -> Any:
        ... 


class Attachment:
    """
    Cython implementation of _Attachment

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::QcMLFile_1_1Attachment.html>`_
    """
    
    name: Union[bytes, str, String]
    
    id: Union[bytes, str, String]
    
    value: Union[bytes, str, String]
    
    cvRef: Union[bytes, str, String]
    
    cvAcc: Union[bytes, str, String]
    
    unitRef: Union[bytes, str, String]
    
    unitAcc: Union[bytes, str, String]
    
    binary: Union[bytes, str, String]
    
    qualityRef: Union[bytes, str, String]
    
    colTypes: List[bytes]
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void Attachment()
        """
        ...
    
    @overload
    def __init__(self, in_0: Attachment ) -> None:
        """
        Cython signature: void Attachment(Attachment &)
        """
        ...
    
    def toXMLString(self, indentation_level: int ) -> Union[bytes, str, String]:
        """
        Cython signature: String toXMLString(unsigned int indentation_level)
        """
        ...
    
    def toCSVString(self, separator: Union[bytes, str, String] ) -> Union[bytes, str, String]:
        """
        Cython signature: String toCSVString(String separator)
        """
        ...
    
    def __richcmp__(self, other: Attachment, op: int) -> Any:
        ... 


class CVReference:
    """
    Cython implementation of _CVReference

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1CVReference.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void CVReference()
        """
        ...
    
    @overload
    def __init__(self, in_0: CVReference ) -> None:
        """
        Cython signature: void CVReference(CVReference &)
        """
        ...
    
    def setName(self, name: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String & name)
        Sets the name of the CV reference
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name of the CV reference
        """
        ...
    
    def setIdentifier(self, identifier: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setIdentifier(const String & identifier)
        Sets the CV identifier which is referenced
        """
        ...
    
    def getIdentifier(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getIdentifier()
        Returns the CV identifier which is referenced
        """
        ...
    
    def __richcmp__(self, other: CVReference, op: int) -> Any:
        ... 


class CachedmzML:
    """
    Cython implementation of _CachedmzML

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1CachedmzML.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void CachedmzML()
        A class that uses on-disk caching to read and write spectra and chromatograms
        """
        ...
    
    @overload
    def __init__(self, in_0: CachedmzML ) -> None:
        """
        Cython signature: void CachedmzML(CachedmzML &)
        """
        ...
    
    @overload
    def __init__(self, filename: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void CachedmzML(String filename)
        """
        ...
    
    def getNrSpectra(self) -> int:
        """
        Cython signature: size_t getNrSpectra()
        """
        ...
    
    def getNrChromatograms(self) -> int:
        """
        Cython signature: size_t getNrChromatograms()
        """
        ...
    
    def getSpectrum(self, idx: int ) -> MSSpectrum:
        """
        Cython signature: MSSpectrum getSpectrum(size_t idx)
        """
        ...
    
    def getChromatogram(self, idx: int ) -> MSChromatogram:
        """
        Cython signature: MSChromatogram getChromatogram(size_t idx)
        """
        ...
    
    def getMetaData(self) -> MSExperiment:
        """
        Cython signature: MSExperiment getMetaData()
        """
        ...
    
    load: __static_CachedmzML_load
    
    store: __static_CachedmzML_store 


class ChannelInfo:
    """
    Cython implementation of _ChannelInfo

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ChannelInfo.html>`_
    """
    
    description: bytes
    
    name: int
    
    id: int
    
    center: float
    
    active: bool 


class ChromatogramExtractor:
    """
    Cython implementation of _ChromatogramExtractor

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ChromatogramExtractor.html>`_
      -- Inherits from ['ProgressLogger']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ChromatogramExtractor()
        """
        ...
    
    @overload
    def __init__(self, in_0: ChromatogramExtractor ) -> None:
        """
        Cython signature: void ChromatogramExtractor(ChromatogramExtractor &)
        """
        ...
    
    def extractChromatograms(self, input: MSExperiment , output: MSExperiment , transition_exp: TargetedExperiment , extract_window: float , ppm: bool , trafo: TransformationDescription , rt_extraction_window: float , filter: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void extractChromatograms(MSExperiment & input, MSExperiment & output, TargetedExperiment & transition_exp, double extract_window, bool ppm, TransformationDescription trafo, double rt_extraction_window, String filter)
        Extract chromatograms at the m/z and RT defined by the ExtractionCoordinates
        """
        ...
    
    def setLogType(self, in_0: int ) -> None:
        """
        Cython signature: void setLogType(LogType)
        Sets the progress log that should be used. The default type is NONE!
        """
        ...
    
    def getLogType(self) -> int:
        """
        Cython signature: LogType getLogType()
        Returns the type of progress log being used
        """
        ...
    
    def startProgress(self, begin: int , end: int , label: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)
        """
        ...
    
    def setProgress(self, value: int ) -> None:
        """
        Cython signature: void setProgress(ptrdiff_t value)
        Sets the current progress
        """
        ...
    
    def endProgress(self) -> None:
        """
        Cython signature: void endProgress()
        Ends the progress display
        """
        ...
    
    def nextProgress(self) -> None:
        """
        Cython signature: void nextProgress()
        Increment progress by 1 (according to range begin-end)
        """
        ... 


class ChromatogramSettings:
    """
    Cython implementation of _ChromatogramSettings

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ChromatogramSettings.html>`_
      -- Inherits from ['MetaInfoInterface']

    Description of the chromatogram settings, provides meta-information
    about a single chromatogram.
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ChromatogramSettings()
        """
        ...
    
    @overload
    def __init__(self, in_0: ChromatogramSettings ) -> None:
        """
        Cython signature: void ChromatogramSettings(ChromatogramSettings &)
        """
        ...
    
    def getProduct(self) -> Product:
        """
        Cython signature: Product getProduct()
        Returns the product ion
        """
        ...
    
    def setProduct(self, p: Product ) -> None:
        """
        Cython signature: void setProduct(Product p)
        Sets the product ion
        """
        ...
    
    def getNativeID(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getNativeID()
        Returns the native identifier for the spectrum, used by the acquisition software.
        """
        ...
    
    def setNativeID(self, native_id: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setNativeID(String native_id)
        Sets the native identifier for the spectrum, used by the acquisition software.
        """
        ...
    
    def getComment(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getComment()
        Returns the free-text comment
        """
        ...
    
    def setComment(self, comment: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setComment(String comment)
        Sets the free-text comment
        """
        ...
    
    def getInstrumentSettings(self) -> InstrumentSettings:
        """
        Cython signature: InstrumentSettings getInstrumentSettings()
        Returns the instrument settings of the current spectrum
        """
        ...
    
    def setInstrumentSettings(self, instrument_settings: InstrumentSettings ) -> None:
        """
        Cython signature: void setInstrumentSettings(InstrumentSettings instrument_settings)
        Sets the instrument settings of the current spectrum
        """
        ...
    
    def getAcquisitionInfo(self) -> AcquisitionInfo:
        """
        Cython signature: AcquisitionInfo getAcquisitionInfo()
        Returns the acquisition info
        """
        ...
    
    def setAcquisitionInfo(self, acquisition_info: AcquisitionInfo ) -> None:
        """
        Cython signature: void setAcquisitionInfo(AcquisitionInfo acquisition_info)
        Sets the acquisition info
        """
        ...
    
    def getSourceFile(self) -> SourceFile:
        """
        Cython signature: SourceFile getSourceFile()
        Returns the source file
        """
        ...
    
    def setSourceFile(self, source_file: SourceFile ) -> None:
        """
        Cython signature: void setSourceFile(SourceFile source_file)
        Sets the source file
        """
        ...
    
    def getPrecursor(self) -> Precursor:
        """
        Cython signature: Precursor getPrecursor()
        Returns the precursors
        """
        ...
    
    def setPrecursor(self, precursor: Precursor ) -> None:
        """
        Cython signature: void setPrecursor(Precursor precursor)
        Sets the precursors
        """
        ...
    
    def getDataProcessing(self) -> List[DataProcessing]:
        """
        Cython signature: libcpp_vector[shared_ptr[DataProcessing]] getDataProcessing()
        Returns the description of the applied processing
        """
        ...
    
    def setDataProcessing(self, in_0: List[DataProcessing] ) -> None:
        """
        Cython signature: void setDataProcessing(libcpp_vector[shared_ptr[DataProcessing]])
        Sets the description of the applied processing
        """
        ...
    
    def setChromatogramType(self, type: int ) -> None:
        """
        Cython signature: void setChromatogramType(ChromatogramType type)
        Sets the chromatogram type
        """
        ...
    
    def getChromatogramType(self) -> int:
        """
        Cython signature: ChromatogramType getChromatogramType()
        Get the chromatogram type
        """
        ...
    
    def isMetaEmpty(self) -> bool:
        """
        Cython signature: bool isMetaEmpty()
        Returns if the MetaInfo is empty
        """
        ...
    
    def clearMetaInfo(self) -> None:
        """
        Cython signature: void clearMetaInfo()
        Removes all meta values
        """
        ...
    
    def metaRegistry(self) -> MetaInfoRegistry:
        """
        Cython signature: MetaInfoRegistry metaRegistry()
        Returns a reference to the MetaInfoRegistry
        """
        ...
    
    def getKeys(self, keys: List[bytes] ) -> None:
        """
        Cython signature: void getKeys(libcpp_vector[String] & keys)
        Fills the given vector with a list of all keys for which a value is set
        """
        ...
    
    def getMetaValue(self, in_0: Union[bytes, str, String] ) -> Union[int, float, bytes, str, List[int], List[float], List[bytes]]:
        """
        Cython signature: DataValue getMetaValue(String)
        Returns the value corresponding to a string, or
        """
        ...
    
    def setMetaValue(self, in_0: Union[bytes, str, String] , in_1: Union[int, float, bytes, str, List[int], List[float], List[bytes]] ) -> None:
        """
        Cython signature: void setMetaValue(String, DataValue)
        Sets the DataValue corresponding to a name
        """
        ...
    
    def metaValueExists(self, in_0: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool metaValueExists(String)
        Returns whether an entry with the given name exists
        """
        ...
    
    def removeMetaValue(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void removeMetaValue(String)
        Removes the DataValue corresponding to `name` if it exists
        """
        ...
    
    def __richcmp__(self, other: ChromatogramSettings, op: int) -> Any:
        ...
    ChromatogramType : __ChromatogramType 


class ConsensusIDAlgorithmAverage:
    """
    Cython implementation of _ConsensusIDAlgorithmAverage

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ConsensusIDAlgorithmAverage.html>`_
      -- Inherits from ['ConsensusIDAlgorithmIdentity']
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void ConsensusIDAlgorithmAverage()
        """
        ...
    
    def apply(self, ids: List[PeptideIdentification] , number_of_runs: int ) -> None:
        """
        Cython signature: void apply(libcpp_vector[PeptideIdentification] & ids, size_t number_of_runs)
        Calculates the consensus ID for a set of peptide identifications of one spectrum or (consensus) feature
        """
        ...
    
    def getSubsections(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getSubsections()
        """
        ...
    
    def setParameters(self, param: Param ) -> None:
        """
        Cython signature: void setParameters(Param & param)
        Sets the parameters
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        Returns the parameters
        """
        ...
    
    def getDefaults(self) -> Param:
        """
        Cython signature: Param getDefaults()
        Returns the default parameters
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name
        """
        ...
    
    def setName(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String &)
        Sets the name
        """
        ... 


class ConsensusIDAlgorithmPEPMatrix:
    """
    Cython implementation of _ConsensusIDAlgorithmPEPMatrix

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ConsensusIDAlgorithmPEPMatrix.html>`_
      -- Inherits from ['ConsensusIDAlgorithmSimilarity']
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void ConsensusIDAlgorithmPEPMatrix()
        """
        ...
    
    def apply(self, ids: List[PeptideIdentification] , number_of_runs: int ) -> None:
        """
        Cython signature: void apply(libcpp_vector[PeptideIdentification] & ids, size_t number_of_runs)
        Calculates the consensus ID for a set of peptide identifications of one spectrum or (consensus) feature
        """
        ...
    
    def getSubsections(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getSubsections()
        """
        ...
    
    def setParameters(self, param: Param ) -> None:
        """
        Cython signature: void setParameters(Param & param)
        Sets the parameters
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        Returns the parameters
        """
        ...
    
    def getDefaults(self) -> Param:
        """
        Cython signature: Param getDefaults()
        Returns the default parameters
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name
        """
        ...
    
    def setName(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String &)
        Sets the name
        """
        ... 


class ContactPerson:
    """
    Cython implementation of _ContactPerson

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ContactPerson.html>`_
      -- Inherits from ['MetaInfoInterface']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ContactPerson()
        """
        ...
    
    @overload
    def __init__(self, in_0: ContactPerson ) -> None:
        """
        Cython signature: void ContactPerson(ContactPerson &)
        """
        ...
    
    def getFirstName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getFirstName()
        Returns the first name of the person
        """
        ...
    
    def setFirstName(self, name: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setFirstName(String name)
        Sets the first name of the person
        """
        ...
    
    def getLastName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getLastName()
        Returns the last name of the person
        """
        ...
    
    def setLastName(self, name: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setLastName(String name)
        Sets the last name of the person
        """
        ...
    
    def setName(self, name: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(String name)
        Sets the full name of the person (gets split into first and last name internally)
        """
        ...
    
    def getInstitution(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getInstitution()
        Returns the affiliation
        """
        ...
    
    def setInstitution(self, institution: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setInstitution(String institution)
        Sets the affiliation
        """
        ...
    
    def getEmail(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getEmail()
        Returns the email address
        """
        ...
    
    def setEmail(self, email: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setEmail(String email)
        Sets the email address
        """
        ...
    
    def getURL(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getURL()
        Returns the URL associated with the contact person (e.g., the institute webpage
        """
        ...
    
    def setURL(self, email: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setURL(String email)
        Sets the URL associated with the contact person (e.g., the institute webpage
        """
        ...
    
    def getAddress(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getAddress()
        Returns the address
        """
        ...
    
    def setAddress(self, email: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setAddress(String email)
        Sets the address
        """
        ...
    
    def getContactInfo(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getContactInfo()
        Returns miscellaneous info about the contact person
        """
        ...
    
    def setContactInfo(self, contact_info: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setContactInfo(String contact_info)
        Sets miscellaneous info about the contact person
        """
        ...
    
    def isMetaEmpty(self) -> bool:
        """
        Cython signature: bool isMetaEmpty()
        Returns if the MetaInfo is empty
        """
        ...
    
    def clearMetaInfo(self) -> None:
        """
        Cython signature: void clearMetaInfo()
        Removes all meta values
        """
        ...
    
    def metaRegistry(self) -> MetaInfoRegistry:
        """
        Cython signature: MetaInfoRegistry metaRegistry()
        Returns a reference to the MetaInfoRegistry
        """
        ...
    
    def getKeys(self, keys: List[bytes] ) -> None:
        """
        Cython signature: void getKeys(libcpp_vector[String] & keys)
        Fills the given vector with a list of all keys for which a value is set
        """
        ...
    
    def getMetaValue(self, in_0: Union[bytes, str, String] ) -> Union[int, float, bytes, str, List[int], List[float], List[bytes]]:
        """
        Cython signature: DataValue getMetaValue(String)
        Returns the value corresponding to a string, or
        """
        ...
    
    def setMetaValue(self, in_0: Union[bytes, str, String] , in_1: Union[int, float, bytes, str, List[int], List[float], List[bytes]] ) -> None:
        """
        Cython signature: void setMetaValue(String, DataValue)
        Sets the DataValue corresponding to a name
        """
        ...
    
    def metaValueExists(self, in_0: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool metaValueExists(String)
        Returns whether an entry with the given name exists
        """
        ...
    
    def removeMetaValue(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void removeMetaValue(String)
        Removes the DataValue corresponding to `name` if it exists
        """
        ...
    
    def __richcmp__(self, other: ContactPerson, op: int) -> Any:
        ... 


class CsiAdapterHit:
    """
    Cython implementation of _CsiAdapterHit

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::CsiFingerIdMzTabWriter_1_1CsiAdapterHit.html>`_
    """
    
    inchikey2D: Union[bytes, str, String]
    
    inchi: Union[bytes, str, String]
    
    rank: int
    
    formula_rank: int
    
    adduct: Union[bytes, str, String]
    
    molecular_formula: Union[bytes, str, String]
    
    score: float
    
    name: Union[bytes, str, String]
    
    smiles: Union[bytes, str, String]
    
    xlogp: Union[bytes, str, String]
    
    dbflags: Union[bytes, str, String]
    
    pubchemids: List[bytes]
    
    links: List[bytes]
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void CsiAdapterHit()
        """
        ...
    
    @overload
    def __init__(self, in_0: CsiAdapterHit ) -> None:
        """
        Cython signature: void CsiAdapterHit(CsiAdapterHit &)
        """
        ... 


class DTA2DFile:
    """
    Cython implementation of _DTA2DFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1DTA2DFile.html>`_
      -- Inherits from ['ProgressLogger']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void DTA2DFile()
        """
        ...
    
    @overload
    def __init__(self, in_0: DTA2DFile ) -> None:
        """
        Cython signature: void DTA2DFile(DTA2DFile &)
        """
        ...
    
    def storeTIC(self, filename: Union[bytes, str, String] , peakmap: MSExperiment ) -> None:
        """
        Cython signature: void storeTIC(String filename, MSExperiment & peakmap)
        """
        ...
    
    def store(self, filename: Union[bytes, str, String] , peakmap: MSExperiment ) -> None:
        """
        Cython signature: void store(String filename, MSExperiment & peakmap)
        """
        ...
    
    def load(self, filename: Union[bytes, str, String] , peakmap: MSExperiment ) -> None:
        """
        Cython signature: void load(String filename, MSExperiment & peakmap)
        """
        ...
    
    def getOptions(self) -> PeakFileOptions:
        """
        Cython signature: PeakFileOptions getOptions()
        """
        ...
    
    def setLogType(self, in_0: int ) -> None:
        """
        Cython signature: void setLogType(LogType)
        Sets the progress log that should be used. The default type is NONE!
        """
        ...
    
    def getLogType(self) -> int:
        """
        Cython signature: LogType getLogType()
        Returns the type of progress log being used
        """
        ...
    
    def startProgress(self, begin: int , end: int , label: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)
        """
        ...
    
    def setProgress(self, value: int ) -> None:
        """
        Cython signature: void setProgress(ptrdiff_t value)
        Sets the current progress
        """
        ...
    
    def endProgress(self) -> None:
        """
        Cython signature: void endProgress()
        Ends the progress display
        """
        ...
    
    def nextProgress(self) -> None:
        """
        Cython signature: void nextProgress()
        Increment progress by 1 (according to range begin-end)
        """
        ... 


class DataFilter:
    """
    Cython implementation of _DataFilter

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1DataFilter.html>`_
    """
    
    field: int
    
    op: int
    
    value: float
    
    value_string: Union[bytes, str, String]
    
    meta_name: Union[bytes, str, String]
    
    value_is_numerical: bool
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void DataFilter()
        """
        ...
    
    @overload
    def __init__(self, in_0: DataFilter ) -> None:
        """
        Cython signature: void DataFilter(DataFilter &)
        """
        ...
    
    def toString(self) -> Union[bytes, str, String]:
        """
        Cython signature: String toString()
        """
        ...
    
    def fromString(self, filter_: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void fromString(const String & filter_)
        """
        ...
    
    def __str__(self) -> Union[bytes, str, String]:
        """
        Cython signature: String toString()
        """
        ...
    
    def __richcmp__(self, other: DataFilter, op: int) -> Any:
        ... 


class DataFilters:
    """
    Cython implementation of _DataFilters

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1DataFilters.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void DataFilters()
        """
        ...
    
    @overload
    def __init__(self, in_0: DataFilters ) -> None:
        """
        Cython signature: void DataFilters(DataFilters &)
        """
        ...
    
    def size(self) -> int:
        """
        Cython signature: size_t size()
        """
        ...
    
    def __getitem__(self, in_0: int ) -> DataFilter:
        """
        Cython signature: DataFilter operator[](size_t)
        """
        ...
    
    def add(self, filter_: DataFilter ) -> None:
        """
        Cython signature: void add(DataFilter & filter_)
        """
        ...
    
    def remove(self, index: int ) -> None:
        """
        Cython signature: void remove(size_t index)
        """
        ...
    
    def replace(self, index: int , filter_: DataFilter ) -> None:
        """
        Cython signature: void replace(size_t index, DataFilter & filter_)
        """
        ...
    
    def clear(self) -> None:
        """
        Cython signature: void clear()
        """
        ...
    
    def setActive(self, is_active: bool ) -> None:
        """
        Cython signature: void setActive(bool is_active)
        """
        ...
    
    def isActive(self) -> bool:
        """
        Cython signature: bool isActive()
        """
        ...
    
    @overload
    def passes(self, feature: Feature ) -> bool:
        """
        Cython signature: bool passes(Feature & feature)
        """
        ...
    
    @overload
    def passes(self, consensus_feature: ConsensusFeature ) -> bool:
        """
        Cython signature: bool passes(ConsensusFeature & consensus_feature)
        """
        ...
    
    @overload
    def passes(self, spectrum: MSSpectrum , peak_index: int ) -> bool:
        """
        Cython signature: bool passes(MSSpectrum & spectrum, size_t peak_index)
        """
        ...
    FilterOperation : __FilterOperation
    FilterType : __FilterType 


class Deisotoper:
    """
    Cython implementation of _Deisotoper

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1Deisotoper.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void Deisotoper()
        """
        ...
    
    @overload
    def __init__(self, in_0: Deisotoper ) -> None:
        """
        Cython signature: void Deisotoper(Deisotoper &)
        """
        ...
    
    deisotopeAndSingleCharge: __static_Deisotoper_deisotopeAndSingleCharge
    
    deisotopeAndSingleChargeDefault: __static_Deisotoper_deisotopeAndSingleChargeDefault
    
    deisotopeWithAveragineModel: __static_Deisotoper_deisotopeWithAveragineModel 


class Digestion:
    """
    Cython implementation of _Digestion

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1Digestion.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void Digestion()
        """
        ...
    
    @overload
    def __init__(self, in_0: Digestion ) -> None:
        """
        Cython signature: void Digestion(Digestion &)
        """
        ...
    
    def getEnzyme(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getEnzyme()
        Returns the enzyme name (default is "")
        """
        ...
    
    def setEnzyme(self, enzyme: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setEnzyme(const String & enzyme)
        Sets the enzyme name
        """
        ...
    
    def getDigestionTime(self) -> float:
        """
        Cython signature: double getDigestionTime()
        Returns the digestion time in minutes (default is 0.0)
        """
        ...
    
    def setDigestionTime(self, digestion_time: float ) -> None:
        """
        Cython signature: void setDigestionTime(double digestion_time)
        Sets the digestion time in minutes
        """
        ...
    
    def getTemperature(self) -> float:
        """
        Cython signature: double getTemperature()
        Returns the temperature during digestion in degree C (default is 0.0)
        """
        ...
    
    def setTemperature(self, temperature: float ) -> None:
        """
        Cython signature: void setTemperature(double temperature)
        Sets the temperature during digestion in degree C
        """
        ...
    
    def getPh(self) -> float:
        """
        Cython signature: double getPh()
        Returns the pH value (default is 0.0)
        """
        ...
    
    def setPh(self, ph: float ) -> None:
        """
        Cython signature: void setPh(double ph)
        Sets the pH value
        """
        ... 


class DistanceMatrix:
    """
    Cython implementation of _DistanceMatrix[float]

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1DistanceMatrix[float].html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void DistanceMatrix()
        """
        ...
    
    @overload
    def __init__(self, in_0: DistanceMatrix ) -> None:
        """
        Cython signature: void DistanceMatrix(DistanceMatrix &)
        """
        ...
    
    @overload
    def __init__(self, dimensionsize: int , value: float ) -> None:
        """
        Cython signature: void DistanceMatrix(size_t dimensionsize, float value)
        """
        ...
    
    def getValue(self, i: int , j: int ) -> float:
        """
        Cython signature: float getValue(size_t i, size_t j)
        """
        ...
    
    def setValue(self, i: int , j: int , value: float ) -> None:
        """
        Cython signature: void setValue(size_t i, size_t j, float value)
        """
        ...
    
    def setValueQuick(self, i: int , j: int , value: float ) -> None:
        """
        Cython signature: void setValueQuick(size_t i, size_t j, float value)
        """
        ...
    
    def clear(self) -> None:
        """
        Cython signature: void clear()
        """
        ...
    
    def resize(self, dimensionsize: int , value: float ) -> None:
        """
        Cython signature: void resize(size_t dimensionsize, float value)
        """
        ...
    
    def reduce(self, j: int ) -> None:
        """
        Cython signature: void reduce(size_t j)
        """
        ...
    
    def dimensionsize(self) -> int:
        """
        Cython signature: size_t dimensionsize()
        """
        ...
    
    def updateMinElement(self) -> None:
        """
        Cython signature: void updateMinElement()
        """
        ...
    
    def getMinElementCoordinates(self) -> List[int, int]:
        """
        Cython signature: libcpp_pair[size_t,size_t] getMinElementCoordinates()
        """
        ...
    
    def __richcmp__(self, other: DistanceMatrix, op: int) -> Any:
        ... 


class FeatureGroupingAlgorithm:
    """
    Cython implementation of _FeatureGroupingAlgorithm

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureGroupingAlgorithm.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    def transferSubelements(self, maps: List[ConsensusMap] , out: ConsensusMap ) -> None:
        """
        Cython signature: void transferSubelements(libcpp_vector[ConsensusMap] maps, ConsensusMap & out)
        Transfers subelements (grouped features) from input consensus maps to the result consensus map
        """
        ...
    
    def registerChildren(self) -> None:
        """
        Cython signature: void registerChildren()
        Register all derived classes in this method
        """
        ...
    
    def getSubsections(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getSubsections()
        """
        ...
    
    def setParameters(self, param: Param ) -> None:
        """
        Cython signature: void setParameters(Param & param)
        Sets the parameters
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        Returns the parameters
        """
        ...
    
    def getDefaults(self) -> Param:
        """
        Cython signature: Param getDefaults()
        Returns the default parameters
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name
        """
        ...
    
    def setName(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String &)
        Sets the name
        """
        ... 


class File:
    """
    Cython implementation of _File

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1File.html>`_
    """
    
    absolutePath: __static_File_absolutePath
    
    basename: __static_File_basename
    
    empty: __static_File_empty
    
    exists: __static_File_exists
    
    fileList: __static_File_fileList
    
    find: __static_File_find
    
    findDatabase: __static_File_findDatabase
    
    findDoc: __static_File_findDoc
    
    findExecutable: __static_File_findExecutable
    
    getExecutablePath: __static_File_getExecutablePath
    
    getOpenMSDataPath: __static_File_getOpenMSDataPath
    
    getOpenMSHomePath: __static_File_getOpenMSHomePath
    
    getSystemParameters: __static_File_getSystemParameters
    
    getTempDirectory: __static_File_getTempDirectory
    
    getTemporaryFile: __static_File_getTemporaryFile
    
    getUniqueName: __static_File_getUniqueName
    
    getUserDirectory: __static_File_getUserDirectory
    
    isDirectory: __static_File_isDirectory
    
    path: __static_File_path
    
    readable: __static_File_readable
    
    remove: __static_File_remove
    
    removeDirRecursively: __static_File_removeDirRecursively
    
    rename: __static_File_rename
    
    writable: __static_File_writable 


class FloatDataArray:
    """
    Cython implementation of _FloatDataArray

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::DataArrays_1_1FloatDataArray.html>`_
      -- Inherits from ['MetaInfoDescription']

    The representation of extra float data attached to a spectrum or chromatogram.
    Raw data access is proved by `get_peaks` and `set_peaks`, which yields numpy arrays
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void FloatDataArray()
        """
        ...
    
    @overload
    def __init__(self, in_0: FloatDataArray ) -> None:
        """
        Cython signature: void FloatDataArray(FloatDataArray &)
        """
        ...
    
    def size(self) -> int:
        """
        Cython signature: size_t size()
        """
        ...
    
    def resize(self, n: int ) -> None:
        """
        Cython signature: void resize(size_t n)
        """
        ...
    
    def reserve(self, n: int ) -> None:
        """
        Cython signature: void reserve(size_t n)
        """
        ...
    
    def clear(self) -> None:
        """
        Cython signature: void clear()
        """
        ...
    
    def push_back(self, in_0: float ) -> None:
        """
        Cython signature: void push_back(float)
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name of the peak annotations
        """
        ...
    
    def setName(self, name: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(String name)
        Sets the name of the peak annotations
        """
        ...
    
    def getDataProcessing(self) -> List[DataProcessing]:
        """
        Cython signature: libcpp_vector[shared_ptr[DataProcessing]] getDataProcessing()
        Returns a reference to the description of the applied processing
        """
        ...
    
    def setDataProcessing(self, in_0: List[DataProcessing] ) -> None:
        """
        Cython signature: void setDataProcessing(libcpp_vector[shared_ptr[DataProcessing]])
        Sets the description of the applied processing
        """
        ...
    
    def isMetaEmpty(self) -> bool:
        """
        Cython signature: bool isMetaEmpty()
        Returns if the MetaInfo is empty
        """
        ...
    
    def clearMetaInfo(self) -> None:
        """
        Cython signature: void clearMetaInfo()
        Removes all meta values
        """
        ...
    
    def metaRegistry(self) -> MetaInfoRegistry:
        """
        Cython signature: MetaInfoRegistry metaRegistry()
        Returns a reference to the MetaInfoRegistry
        """
        ...
    
    def getKeys(self, keys: List[bytes] ) -> None:
        """
        Cython signature: void getKeys(libcpp_vector[String] & keys)
        Fills the given vector with a list of all keys for which a value is set
        """
        ...
    
    def getMetaValue(self, in_0: Union[bytes, str, String] ) -> Union[int, float, bytes, str, List[int], List[float], List[bytes]]:
        """
        Cython signature: DataValue getMetaValue(String)
        Returns the value corresponding to a string, or
        """
        ...
    
    def setMetaValue(self, in_0: Union[bytes, str, String] , in_1: Union[int, float, bytes, str, List[int], List[float], List[bytes]] ) -> None:
        """
        Cython signature: void setMetaValue(String, DataValue)
        Sets the DataValue corresponding to a name
        """
        ...
    
    def metaValueExists(self, in_0: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool metaValueExists(String)
        Returns whether an entry with the given name exists
        """
        ...
    
    def removeMetaValue(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void removeMetaValue(String)
        Removes the DataValue corresponding to `name` if it exists
        """
        ...
    
    def __richcmp__(self, other: FloatDataArray, op: int) -> Any:
        ... 


class GNPSMetaValueFile:
    """
    Cython implementation of _GNPSMetaValueFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1GNPSMetaValueFile.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void GNPSMetaValueFile()
        """
        ...
    
    @overload
    def __init__(self, in_0: GNPSMetaValueFile ) -> None:
        """
        Cython signature: void GNPSMetaValueFile(GNPSMetaValueFile &)
        """
        ...
    
    def store(self, consensus_map: ConsensusMap , output_file: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void store(const ConsensusMap & consensus_map, const String & output_file)
        Write meta value table (tsv file) from a list of mzML files. Required for GNPS FBMN.
        
        This will produce the minimal required meta values and can be extended manually.
        
        :param consensus_map: Input ConsensusMap from which the input mzML files will be determined.
        :param output_file: Output file path for the meta value table.
        """
        ... 


class Identification:
    """
    Cython implementation of _Identification

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1Identification.html>`_
      -- Inherits from ['MetaInfoInterface']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void Identification()
        Represents a object which can store the information of an analysisXML instance
        """
        ...
    
    @overload
    def __init__(self, in_0: Identification ) -> None:
        """
        Cython signature: void Identification(Identification &)
        """
        ...
    
    def setCreationDate(self, date: DateTime ) -> None:
        """
        Cython signature: void setCreationDate(DateTime date)
        Sets the date and time the file was written
        """
        ...
    
    def getCreationDate(self) -> DateTime:
        """
        Cython signature: DateTime getCreationDate()
        Returns the date and time the file was created
        """
        ...
    
    def setSpectrumIdentifications(self, ids: List[SpectrumIdentification] ) -> None:
        """
        Cython signature: void setSpectrumIdentifications(libcpp_vector[SpectrumIdentification] & ids)
        Sets the spectrum identifications
        """
        ...
    
    def addSpectrumIdentification(self, id: SpectrumIdentification ) -> None:
        """
        Cython signature: void addSpectrumIdentification(SpectrumIdentification & id)
        Adds a spectrum identification
        """
        ...
    
    def getSpectrumIdentifications(self) -> List[SpectrumIdentification]:
        """
        Cython signature: libcpp_vector[SpectrumIdentification] getSpectrumIdentifications()
        Returns the spectrum identifications stored
        """
        ...
    
    def isMetaEmpty(self) -> bool:
        """
        Cython signature: bool isMetaEmpty()
        Returns if the MetaInfo is empty
        """
        ...
    
    def clearMetaInfo(self) -> None:
        """
        Cython signature: void clearMetaInfo()
        Removes all meta values
        """
        ...
    
    def metaRegistry(self) -> MetaInfoRegistry:
        """
        Cython signature: MetaInfoRegistry metaRegistry()
        Returns a reference to the MetaInfoRegistry
        """
        ...
    
    def getKeys(self, keys: List[bytes] ) -> None:
        """
        Cython signature: void getKeys(libcpp_vector[String] & keys)
        Fills the given vector with a list of all keys for which a value is set
        """
        ...
    
    def getMetaValue(self, in_0: Union[bytes, str, String] ) -> Union[int, float, bytes, str, List[int], List[float], List[bytes]]:
        """
        Cython signature: DataValue getMetaValue(String)
        Returns the value corresponding to a string, or
        """
        ...
    
    def setMetaValue(self, in_0: Union[bytes, str, String] , in_1: Union[int, float, bytes, str, List[int], List[float], List[bytes]] ) -> None:
        """
        Cython signature: void setMetaValue(String, DataValue)
        Sets the DataValue corresponding to a name
        """
        ...
    
    def metaValueExists(self, in_0: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool metaValueExists(String)
        Returns whether an entry with the given name exists
        """
        ...
    
    def removeMetaValue(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void removeMetaValue(String)
        Removes the DataValue corresponding to `name` if it exists
        """
        ...
    
    def __richcmp__(self, other: Identification, op: int) -> Any:
        ... 


class IndexedMzMLFileLoader:
    """
    Cython implementation of _IndexedMzMLFileLoader

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1IndexedMzMLFileLoader.html>`_
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void IndexedMzMLFileLoader()
        A class to load an indexedmzML file
        """
        ...
    
    def load(self, in_0: Union[bytes, str, String] , in_1: OnDiscMSExperiment ) -> bool:
        """
        Cython signature: bool load(String, OnDiscMSExperiment &)
        Load a file\n
        
        Tries to parse the file, success needs to be checked with the return value
        """
        ...
    
    @overload
    def store(self, in_0: Union[bytes, str, String] , in_1: OnDiscMSExperiment ) -> None:
        """
        Cython signature: void store(String, OnDiscMSExperiment &)
        Store a file from an on-disc data-structure
        
        
        :param filename: Filename determines where the file will be stored
        :param exp: MS data to be stored
        """
        ...
    
    @overload
    def store(self, in_0: Union[bytes, str, String] , in_1: MSExperiment ) -> None:
        """
        Cython signature: void store(String, MSExperiment &)
        Store a file from an in-memory data-structure
        
        
        :param filename: Filename determines where the file will be stored
        :param exp: MS data to be stored
        """
        ...
    
    def getOptions(self) -> PeakFileOptions:
        """
        Cython signature: PeakFileOptions getOptions()
        Returns the options for loading/storing
        """
        ...
    
    def setOptions(self, in_0: PeakFileOptions ) -> None:
        """
        Cython signature: void setOptions(PeakFileOptions)
        Returns the options for loading/storing
        """
        ... 


class IsobaricIsotopeCorrector:
    """
    Cython implementation of _IsobaricIsotopeCorrector

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1IsobaricIsotopeCorrector.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void IsobaricIsotopeCorrector()
        """
        ...
    
    @overload
    def __init__(self, in_0: IsobaricIsotopeCorrector ) -> None:
        """
        Cython signature: void IsobaricIsotopeCorrector(IsobaricIsotopeCorrector &)
        """
        ...
    
    @overload
    def correctIsotopicImpurities(self, consensus_map_in: ConsensusMap , consensus_map_out: ConsensusMap , quant_method: ItraqEightPlexQuantitationMethod ) -> IsobaricQuantifierStatistics:
        """
        Cython signature: IsobaricQuantifierStatistics correctIsotopicImpurities(ConsensusMap & consensus_map_in, ConsensusMap & consensus_map_out, ItraqEightPlexQuantitationMethod * quant_method)
        """
        ...
    
    @overload
    def correctIsotopicImpurities(self, consensus_map_in: ConsensusMap , consensus_map_out: ConsensusMap , quant_method: ItraqFourPlexQuantitationMethod ) -> IsobaricQuantifierStatistics:
        """
        Cython signature: IsobaricQuantifierStatistics correctIsotopicImpurities(ConsensusMap & consensus_map_in, ConsensusMap & consensus_map_out, ItraqFourPlexQuantitationMethod * quant_method)
        """
        ...
    
    @overload
    def correctIsotopicImpurities(self, consensus_map_in: ConsensusMap , consensus_map_out: ConsensusMap , quant_method: TMTSixPlexQuantitationMethod ) -> IsobaricQuantifierStatistics:
        """
        Cython signature: IsobaricQuantifierStatistics correctIsotopicImpurities(ConsensusMap & consensus_map_in, ConsensusMap & consensus_map_out, TMTSixPlexQuantitationMethod * quant_method)
        """
        ...
    
    @overload
    def correctIsotopicImpurities(self, consensus_map_in: ConsensusMap , consensus_map_out: ConsensusMap , quant_method: TMTTenPlexQuantitationMethod ) -> IsobaricQuantifierStatistics:
        """
        Cython signature: IsobaricQuantifierStatistics correctIsotopicImpurities(ConsensusMap & consensus_map_in, ConsensusMap & consensus_map_out, TMTTenPlexQuantitationMethod * quant_method)
        """
        ... 


class IsobaricNormalizer:
    """
    Cython implementation of _IsobaricNormalizer

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1IsobaricNormalizer.html>`_
    """
    
    @overload
    def __init__(self, in_0: IsobaricNormalizer ) -> None:
        """
        Cython signature: void IsobaricNormalizer(IsobaricNormalizer &)
        """
        ...
    
    @overload
    def __init__(self, quant_method: ItraqFourPlexQuantitationMethod ) -> None:
        """
        Cython signature: void IsobaricNormalizer(ItraqFourPlexQuantitationMethod * quant_method)
        """
        ...
    
    @overload
    def __init__(self, quant_method: ItraqEightPlexQuantitationMethod ) -> None:
        """
        Cython signature: void IsobaricNormalizer(ItraqEightPlexQuantitationMethod * quant_method)
        """
        ...
    
    @overload
    def __init__(self, quant_method: TMTSixPlexQuantitationMethod ) -> None:
        """
        Cython signature: void IsobaricNormalizer(TMTSixPlexQuantitationMethod * quant_method)
        """
        ...
    
    @overload
    def __init__(self, quant_method: TMTTenPlexQuantitationMethod ) -> None:
        """
        Cython signature: void IsobaricNormalizer(TMTTenPlexQuantitationMethod * quant_method)
        """
        ...
    
    def normalize(self, consensus_map: ConsensusMap ) -> None:
        """
        Cython signature: void normalize(ConsensusMap & consensus_map)
        """
        ... 


class IsotopeDistributionCache:
    """
    Cython implementation of _IsotopeDistributionCache

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1IsotopeDistributionCache.html>`_
    """
    
    @overload
    def __init__(self, max_mass: float , mass_window_width: float , intensity_percentage: float , intensity_percentage_optional: float ) -> None:
        """
        Cython signature: void IsotopeDistributionCache(double max_mass, double mass_window_width, double intensity_percentage, double intensity_percentage_optional)
        """
        ...
    
    @overload
    def __init__(self, in_0: IsotopeDistributionCache ) -> None:
        """
        Cython signature: void IsotopeDistributionCache(IsotopeDistributionCache &)
        """
        ...
    
    def getIsotopeDistribution(self, mass: float ) -> TheoreticalIsotopePattern:
        """
        Cython signature: TheoreticalIsotopePattern getIsotopeDistribution(double mass)
        Returns the isotope distribution for a certain mass window
        """
        ... 


class IsotopeLabelingMDVs:
    """
    Cython implementation of _IsotopeLabelingMDVs

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1IsotopeLabelingMDVs.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void IsotopeLabelingMDVs()
        """
        ...
    
    @overload
    def __init__(self, in_0: IsotopeLabelingMDVs ) -> None:
        """
        Cython signature: void IsotopeLabelingMDVs(IsotopeLabelingMDVs &)
        """
        ...
    
    def isotopicCorrection(self, normalized_feature: Feature , corrected_feature: Feature , correction_matrix: MatrixDouble , correction_matrix_agent: int ) -> None:
        """
        Cython signature: void isotopicCorrection(const Feature & normalized_feature, Feature & corrected_feature, MatrixDouble & correction_matrix, const DerivatizationAgent & correction_matrix_agent)
        This function performs an isotopic correction to account for unlabeled abundances coming from
        the derivatization agent (e.g., tBDMS) using correction matrix method and is calculated as follows:
        
        
        :param normalized_feature: Feature with normalized values for each component and unlabeled chemical formula for each component group
        :param correction_matrix: Square matrix holding correction factors derived either experimentally or theoretically which describe how spectral peaks of naturally abundant 13C contribute to spectral peaks that overlap (or convolve) the spectral peaks of the corrected MDV of the derivatization agent
        :param correction_matrix_agent: Name of the derivatization agent, the internally stored correction matrix if the name of the agent is supplied, only "TBDMS" is supported for now
        :return: corrected_feature: Feature with corrected values for each component
        """
        ...
    
    def isotopicCorrections(self, normalized_featureMap: FeatureMap , corrected_featureMap: FeatureMap , correction_matrix: MatrixDouble , correction_matrix_agent: int ) -> None:
        """
        Cython signature: void isotopicCorrections(const FeatureMap & normalized_featureMap, FeatureMap & corrected_featureMap, MatrixDouble & correction_matrix, const DerivatizationAgent & correction_matrix_agent)
        This function performs an isotopic correction to account for unlabeled abundances coming from
        the derivatization agent (e.g., tBDMS) using correction matrix method and is calculated as follows:
        
        
        :param normalized_featuremap: FeatureMap with normalized values for each component and unlabeled chemical formula for each component group
        :param correction_matrix: Square matrix holding correction factors derived either experimentally or theoretically which describe how spectral peaks of naturally abundant 13C contribute to spectral peaks that overlap (or convolve) the spectral peaks of the corrected MDV of the derivatization agent
        :param correction_matrix_agent: Name of the derivatization agent, the internally stored correction matrix if the name of the agent is supplied, only "TBDMS" is supported for now
        :return corrected_featuremap: FeatureMap with corrected values for each component
        """
        ...
    
    def calculateIsotopicPurity(self, normalized_feature: Feature , experiment_data: List[float] , isotopic_purity_name: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void calculateIsotopicPurity(const Feature & normalized_feature, const libcpp_vector[double] & experiment_data, const String & isotopic_purity_name)
        This function calculates the isotopic purity of the MDV using the following formula:
        isotopic purity of tracer (atom % 13C) = n / [n + (M + n-1)/(M + n)],
        where n in M+n is represented as the index of the result
        The formula is extracted from "High-resolution 13C metabolic flux analysis",
        Long et al, doi:10.1038/s41596-019-0204-0
        
        
        :param normalized_feature: Feature with normalized values for each component and the number of heavy labeled e.g., carbons. Out is a Feature with the calculated isotopic purity for the component group
        :param experiment_data: Vector of experiment data in percent
        :param isotopic_purity_name: Name of the isotopic purity tracer to be saved as a meta value
        """
        ...
    
    def calculateMDVAccuracy(self, normalized_feature: Feature , feature_name: Union[bytes, str, String] , fragment_isotopomer_theoretical_formula: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void calculateMDVAccuracy(const Feature & normalized_feature, const String & feature_name, const String & fragment_isotopomer_theoretical_formula)
        This function calculates the accuracy of the MDV as compared to the theoretical MDV (only for 12C quality control experiments)
        using average deviation to the mean. The result is mapped to the meta value "average_accuracy" in the updated feature
        
        
        :param normalized_feature: Feature with normalized values for each component and the chemical formula of the component group. Out is a Feature with the component group accuracy and accuracy for the error for each component
        :param fragment_isotopomer_measured: Measured scan values
        :param fragment_isotopomer_theoretical_formula: Empirical formula from which the theoretical values will be generated
        """
        ...
    
    def calculateMDVAccuracies(self, normalized_featureMap: FeatureMap , feature_name: Union[bytes, str, String] , fragment_isotopomer_theoretical_formulas: Dict[Union[bytes, str], Union[bytes, str]] ) -> None:
        """
        Cython signature: void calculateMDVAccuracies(const FeatureMap & normalized_featureMap, const String & feature_name, const libcpp_map[libcpp_utf8_string,libcpp_utf8_string] & fragment_isotopomer_theoretical_formulas)
        This function calculates the accuracy of the MDV as compared to the theoretical MDV (only for 12C quality control experiments)
        using average deviation to the mean
        
        
        param normalized_featuremap: FeatureMap with normalized values for each component and the chemical formula of the component group. Out is a FeatureMap with the component group accuracy and accuracy for the error for each component
        param fragment_isotopomer_measured: Measured scan values
        param fragment_isotopomer_theoretical_formula: A map of ProteinName/peptideRef to Empirical formula from which the theoretical values will be generated
        """
        ...
    
    def calculateMDV(self, measured_feature: Feature , normalized_feature: Feature , mass_intensity_type: int , feature_name: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void calculateMDV(const Feature & measured_feature, Feature & normalized_feature, const MassIntensityType & mass_intensity_type, const String & feature_name)
        """
        ...
    
    def calculateMDVs(self, measured_featureMap: FeatureMap , normalized_featureMap: FeatureMap , mass_intensity_type: int , feature_name: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void calculateMDVs(const FeatureMap & measured_featureMap, FeatureMap & normalized_featureMap, const MassIntensityType & mass_intensity_type, const String & feature_name)
        """
        ... 


class IsotopePattern:
    """
    Cython implementation of _IsotopePattern

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::FeatureFinderAlgorithmPickedHelperStructs_1_1IsotopePattern.html>`_
    """
    
    spectrum: List[int]
    
    intensity: List[float]
    
    mz_score: List[float]
    
    theoretical_mz: List[float]
    
    theoretical_pattern: TheoreticalIsotopePattern
    
    @overload
    def __init__(self, size: int ) -> None:
        """
        Cython signature: void IsotopePattern(size_t size)
        """
        ...
    
    @overload
    def __init__(self, in_0: IsotopePattern ) -> None:
        """
        Cython signature: void IsotopePattern(IsotopePattern &)
        """
        ... 


class ItraqConstants:
    """
    Cython implementation of _ItraqConstants

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ItraqConstants.html>`_

    Some constants used throughout iTRAQ classes
    
    Constants for iTRAQ experiments and a ChannelInfo structure to store information about a single channel
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ItraqConstants()
        """
        ...
    
    @overload
    def __init__(self, in_0: ItraqConstants ) -> None:
        """
        Cython signature: void ItraqConstants(ItraqConstants &)
        """
        ...
    
    def getIsotopeMatrixAsStringList(self, itraq_type: int , isotope_corrections: List[MatrixDouble] ) -> List[bytes]:
        """
        Cython signature: StringList getIsotopeMatrixAsStringList(int itraq_type, libcpp_vector[MatrixDouble] & isotope_corrections)
        Convert isotope correction matrix to stringlist\n
        
        Each line is converted into a string of the format channel:-2Da/-1Da/+1Da/+2Da ; e.g. '114:0/0.3/4/0'
        Useful for creating parameters or debug output
        
        
        :param itraq_type: Which matrix to stringify. Should be of values from enum ITRAQ_TYPES
        :param isotope_corrections: Vector of the two matrices (4plex, 8plex)
        """
        ...
    
    def updateIsotopeMatrixFromStringList(self, itraq_type: int , channels: List[bytes] , isotope_corrections: List[MatrixDouble] ) -> None:
        """
        Cython signature: void updateIsotopeMatrixFromStringList(int itraq_type, StringList & channels, libcpp_vector[MatrixDouble] & isotope_corrections)
        Convert strings to isotope correction matrix rows\n
        
        Each string of format channel:-2Da/-1Da/+1Da/+2Da ; e.g. '114:0/0.3/4/0'
        is parsed and the corresponding channel(row) in the matrix is updated
        Not all channels need to be present, missing channels will be left untouched
        Useful to update the matrix with user isotope correction values
        
        
        :param itraq_type: Which matrix to stringify. Should be of values from enum ITRAQ_TYPES
        :param channels: New channel isotope values as strings
        :param isotope_corrections: Vector of the two matrices (4plex, 8plex)
        """
        ...
    
    def translateIsotopeMatrix(self, itraq_type: int , isotope_corrections: List[MatrixDouble] ) -> MatrixDouble:
        """
        Cython signature: MatrixDouble translateIsotopeMatrix(int & itraq_type, libcpp_vector[MatrixDouble] & isotope_corrections)
        """
        ... 


class ItraqEightPlexQuantitationMethod:
    """
    Cython implementation of _ItraqEightPlexQuantitationMethod

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ItraqEightPlexQuantitationMethod.html>`_
      -- Inherits from ['IsobaricQuantitationMethod']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ItraqEightPlexQuantitationMethod()
        iTRAQ 8 plex quantitation to be used with the IsobaricQuantitation
        """
        ...
    
    @overload
    def __init__(self, in_0: ItraqEightPlexQuantitationMethod ) -> None:
        """
        Cython signature: void ItraqEightPlexQuantitationMethod(ItraqEightPlexQuantitationMethod &)
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        """
        ...
    
    def getChannelInformation(self) -> List[IsobaricChannelInformation]:
        """
        Cython signature: libcpp_vector[IsobaricChannelInformation] getChannelInformation()
        """
        ...
    
    def getNumberOfChannels(self) -> int:
        """
        Cython signature: size_t getNumberOfChannels()
        """
        ...
    
    def getIsotopeCorrectionMatrix(self) -> MatrixDouble:
        """
        Cython signature: MatrixDouble getIsotopeCorrectionMatrix()
        """
        ...
    
    def getReferenceChannel(self) -> int:
        """
        Cython signature: size_t getReferenceChannel()
        """
        ...
    
    def getSubsections(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getSubsections()
        """
        ...
    
    def setParameters(self, param: Param ) -> None:
        """
        Cython signature: void setParameters(Param & param)
        Sets the parameters
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        Returns the parameters
        """
        ...
    
    def getDefaults(self) -> Param:
        """
        Cython signature: Param getDefaults()
        Returns the default parameters
        """
        ...
    
    def setName(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String &)
        Sets the name
        """
        ... 


class JavaInfo:
    """
    Cython implementation of _JavaInfo

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1JavaInfo.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void JavaInfo()
        Detect Java and retrieve information
        """
        ...
    
    @overload
    def __init__(self, in_0: JavaInfo ) -> None:
        """
        Cython signature: void JavaInfo(JavaInfo &)
        """
        ...
    
    def canRun(self, java_executable: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool canRun(String java_executable)
        Determine if Java is installed and reachable\n
        
        The call fails if either Java is not installed or if a relative location is given and Java is not on the search PATH
        
        
        :param java_executable: Path to Java executable. Can be absolute, relative or just a filename
        :return: Returns false if Java executable can not be called; true if Java executable can be executed
        """
        ... 


class MRMFeatureFilter:
    """
    Cython implementation of _MRMFeatureFilter

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMFeatureFilter.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MRMFeatureFilter()
        """
        ...
    
    @overload
    def __init__(self, in_0: MRMFeatureFilter ) -> None:
        """
        Cython signature: void MRMFeatureFilter(MRMFeatureFilter &)
        """
        ...
    
    def FilterFeatureMap(self, features: FeatureMap , filter_criteria: MRMFeatureQC , transitions: TargetedExperiment ) -> None:
        """
        Cython signature: void FilterFeatureMap(FeatureMap features, MRMFeatureQC filter_criteria, TargetedExperiment transitions)
        Flags or filters features and subordinates in a FeatureMap
        
        
        :param features: FeatureMap to flag or filter
        :param filter_criteria: MRMFeatureQC class defining QC parameters
        :param transitions: Transitions from a TargetedExperiment
        """
        ...
    
    def getSubsections(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getSubsections()
        """
        ...
    
    def setParameters(self, param: Param ) -> None:
        """
        Cython signature: void setParameters(Param & param)
        Sets the parameters
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        Returns the parameters
        """
        ...
    
    def getDefaults(self) -> Param:
        """
        Cython signature: Param getDefaults()
        Returns the default parameters
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name
        """
        ...
    
    def setName(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String &)
        Sets the name
        """
        ... 


class MSDataCachedConsumer:
    """
    Cython implementation of _MSDataCachedConsumer

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSDataCachedConsumer.html>`_

    Transforming and cached writing consumer of MS data
    
    Is able to transform a spectrum on the fly while it is read using a
    function pointer that can be set on the object. The spectra is then
    cached to disk using the functions provided in CachedMzMLHandler.
    """
    
    @overload
    def __init__(self, filename: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void MSDataCachedConsumer(String filename)
        """
        ...
    
    @overload
    def __init__(self, filename: Union[bytes, str, String] , clear: bool ) -> None:
        """
        Cython signature: void MSDataCachedConsumer(String filename, bool clear)
        """
        ...
    
    def consumeSpectrum(self, s: MSSpectrum ) -> None:
        """
        Cython signature: void consumeSpectrum(MSSpectrum & s)
        Write a spectrum to the output file
        
        May delete data from spectrum (if clearData is set)
        """
        ...
    
    def consumeChromatogram(self, c: MSChromatogram ) -> None:
        """
        Cython signature: void consumeChromatogram(MSChromatogram & c)
        Write a chromatogram to the output file
        
        May delete data from chromatogram (if clearData is set)
        """
        ...
    
    def setExperimentalSettings(self, exp: ExperimentalSettings ) -> None:
        """
        Cython signature: void setExperimentalSettings(ExperimentalSettings & exp)
        """
        ...
    
    def setExpectedSize(self, expectedSpectra: int , expectedChromatograms: int ) -> None:
        """
        Cython signature: void setExpectedSize(size_t expectedSpectra, size_t expectedChromatograms)
        """
        ... 


class MapAlignmentAlgorithmKD:
    """
    Cython implementation of _MapAlignmentAlgorithmKD

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MapAlignmentAlgorithmKD.html>`_

    An efficient reference-free feature map alignment algorithm for unlabeled data
    
    This algorithm uses a kd-tree to efficiently compute conflict-free connected components (CCC)
    in a compatibility graph on feature data. This graph is comprised of nodes corresponding
    to features and edges connecting features f and f' iff both are within each other's tolerance
    windows (wrt. RT and m/z difference). CCCs are those CCs that do not contain multiple features
    from the same input map, and whose features all have the same charge state
    
    All CCCs above a user-specified minimum size are considered true sets of corresponding features
    and based on these, LOWESS transformations are computed for each input map such that the average
    deviation from the mean retention time within all CCCs is minimized
    """
    
    @overload
    def __init__(self, num_maps: int , param: Param ) -> None:
        """
        Cython signature: void MapAlignmentAlgorithmKD(size_t num_maps, Param & param)
        """
        ...
    
    @overload
    def __init__(self, in_0: MapAlignmentAlgorithmKD ) -> None:
        """
        Cython signature: void MapAlignmentAlgorithmKD(MapAlignmentAlgorithmKD &)
        """
        ...
    
    def addRTFitData(self, kd_data: KDTreeFeatureMaps ) -> None:
        """
        Cython signature: void addRTFitData(KDTreeFeatureMaps & kd_data)
        Compute data points needed for RT transformation in the current `kd_data`, add to `fit_data_`
        """
        ...
    
    def fitLOWESS(self) -> None:
        """
        Cython signature: void fitLOWESS()
        Fit LOWESS to fit_data_, store final models in `transformations_`
        """
        ...
    
    def transform(self, kd_data: KDTreeFeatureMaps ) -> None:
        """
        Cython signature: void transform(KDTreeFeatureMaps & kd_data)
        Transform RTs for `kd_data`
        """
        ... 


class MarkerMower:
    """
    Cython implementation of _MarkerMower

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MarkerMower.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MarkerMower()
        """
        ...
    
    @overload
    def __init__(self, in_0: MarkerMower ) -> None:
        """
        Cython signature: void MarkerMower(MarkerMower &)
        """
        ...
    
    def filterSpectrum(self, spec: MSSpectrum ) -> None:
        """
        Cython signature: void filterSpectrum(MSSpectrum & spec)
        """
        ...
    
    def filterPeakSpectrum(self, spec: MSSpectrum ) -> None:
        """
        Cython signature: void filterPeakSpectrum(MSSpectrum & spec)
        """
        ...
    
    def filterPeakMap(self, exp: MSExperiment ) -> None:
        """
        Cython signature: void filterPeakMap(MSExperiment & exp)
        """
        ...
    
    def getProductName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getProductName()
        Returns the product name
        """
        ...
    
    def insertmarker(self, peak_marker: PeakMarker ) -> None:
        """
        Cython signature: void insertmarker(PeakMarker * peak_marker)
        Insert new Marker (violates the DefaultParamHandler interface)
        """
        ...
    
    def getSubsections(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getSubsections()
        """
        ...
    
    def setParameters(self, param: Param ) -> None:
        """
        Cython signature: void setParameters(Param & param)
        Sets the parameters
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        Returns the parameters
        """
        ...
    
    def getDefaults(self) -> Param:
        """
        Cython signature: Param getDefaults()
        Returns the default parameters
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name
        """
        ...
    
    def setName(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String &)
        Sets the name
        """
        ... 


class MassExplainer:
    """
    Cython implementation of _MassExplainer

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MassExplainer.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MassExplainer()
        Computes empirical formulas for given mass differences using a set of allowed elements
        """
        ...
    
    @overload
    def __init__(self, in_0: MassExplainer ) -> None:
        """
        Cython signature: void MassExplainer(MassExplainer &)
        """
        ...
    
    @overload
    def __init__(self, adduct_base: List[Adduct] ) -> None:
        """
        Cython signature: void MassExplainer(libcpp_vector[Adduct] adduct_base)
        """
        ...
    
    @overload
    def __init__(self, q_min: int , q_max: int , max_span: int , thresh_logp: float ) -> None:
        """
        Cython signature: void MassExplainer(int q_min, int q_max, int max_span, double thresh_logp)
        """
        ...
    
    def setAdductBase(self, adduct_base: List[Adduct] ) -> None:
        """
        Cython signature: void setAdductBase(libcpp_vector[Adduct] adduct_base)
        Sets the set of possible adducts
        """
        ...
    
    def getAdductBase(self) -> List[Adduct]:
        """
        Cython signature: libcpp_vector[Adduct] getAdductBase()
        Returns the set of adducts
        """
        ...
    
    def getCompomerById(self, id: int ) -> Compomer:
        """
        Cython signature: Compomer getCompomerById(size_t id)
        Returns a compomer by its Id (useful after a query() )
        """
        ...
    
    def compute(self) -> None:
        """
        Cython signature: void compute()
        Fill map with possible mass-differences along with their explanation
        """
        ... 


class MassTrace:
    """
    Cython implementation of _MassTrace

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::FeatureFinderAlgorithmPickedHelperStructs_1_1MassTrace.html>`_
    """
    
    max_rt: float
    
    theoretical_int: float
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MassTrace()
        """
        ...
    
    @overload
    def __init__(self, in_0: MassTrace ) -> None:
        """
        Cython signature: void MassTrace(MassTrace &)
        """
        ...
    
    def getConvexhull(self) -> ConvexHull2D:
        """
        Cython signature: ConvexHull2D getConvexhull()
        """
        ...
    
    def updateMaximum(self) -> None:
        """
        Cython signature: void updateMaximum()
        """
        ...
    
    def getAvgMZ(self) -> float:
        """
        Cython signature: double getAvgMZ()
        """
        ...
    
    def isValid(self) -> bool:
        """
        Cython signature: bool isValid()
        """
        ... 


class MassTraces:
    """
    Cython implementation of _MassTraces

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::FeatureFinderAlgorithmPickedHelperStructs_1_1MassTraces.html>`_
    """
    
    max_trace: int
    
    baseline: float
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MassTraces()
        """
        ...
    
    @overload
    def __init__(self, in_0: MassTraces ) -> None:
        """
        Cython signature: void MassTraces(MassTraces &)
        """
        ...
    
    def getPeakCount(self) -> int:
        """
        Cython signature: size_t getPeakCount()
        """
        ...
    
    def isValid(self, seed_mz: float , trace_tolerance: float ) -> bool:
        """
        Cython signature: bool isValid(double seed_mz, double trace_tolerance)
        """
        ...
    
    def getTheoreticalmaxPosition(self) -> int:
        """
        Cython signature: size_t getTheoreticalmaxPosition()
        """
        ...
    
    def updateBaseline(self) -> None:
        """
        Cython signature: void updateBaseline()
        """
        ...
    
    def getRTBounds(self) -> List[float, float]:
        """
        Cython signature: libcpp_pair[double,double] getRTBounds()
        """
        ... 


class MetaInfoDescription:
    """
    Cython implementation of _MetaInfoDescription

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MetaInfoDescription.html>`_
      -- Inherits from ['MetaInfoInterface']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MetaInfoDescription()
        """
        ...
    
    @overload
    def __init__(self, in_0: MetaInfoDescription ) -> None:
        """
        Cython signature: void MetaInfoDescription(MetaInfoDescription &)
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name of the peak annotations
        """
        ...
    
    def setName(self, name: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(String name)
        Sets the name of the peak annotations
        """
        ...
    
    def getDataProcessing(self) -> List[DataProcessing]:
        """
        Cython signature: libcpp_vector[shared_ptr[DataProcessing]] getDataProcessing()
        Returns a reference to the description of the applied processing
        """
        ...
    
    def setDataProcessing(self, in_0: List[DataProcessing] ) -> None:
        """
        Cython signature: void setDataProcessing(libcpp_vector[shared_ptr[DataProcessing]])
        Sets the description of the applied processing
        """
        ...
    
    def isMetaEmpty(self) -> bool:
        """
        Cython signature: bool isMetaEmpty()
        Returns if the MetaInfo is empty
        """
        ...
    
    def clearMetaInfo(self) -> None:
        """
        Cython signature: void clearMetaInfo()
        Removes all meta values
        """
        ...
    
    def metaRegistry(self) -> MetaInfoRegistry:
        """
        Cython signature: MetaInfoRegistry metaRegistry()
        Returns a reference to the MetaInfoRegistry
        """
        ...
    
    def getKeys(self, keys: List[bytes] ) -> None:
        """
        Cython signature: void getKeys(libcpp_vector[String] & keys)
        Fills the given vector with a list of all keys for which a value is set
        """
        ...
    
    def getMetaValue(self, in_0: Union[bytes, str, String] ) -> Union[int, float, bytes, str, List[int], List[float], List[bytes]]:
        """
        Cython signature: DataValue getMetaValue(String)
        Returns the value corresponding to a string, or
        """
        ...
    
    def setMetaValue(self, in_0: Union[bytes, str, String] , in_1: Union[int, float, bytes, str, List[int], List[float], List[bytes]] ) -> None:
        """
        Cython signature: void setMetaValue(String, DataValue)
        Sets the DataValue corresponding to a name
        """
        ...
    
    def metaValueExists(self, in_0: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool metaValueExists(String)
        Returns whether an entry with the given name exists
        """
        ...
    
    def removeMetaValue(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void removeMetaValue(String)
        Removes the DataValue corresponding to `name` if it exists
        """
        ...
    
    def __richcmp__(self, other: MetaInfoDescription, op: int) -> Any:
        ... 


class MetaInfoInterface:
    """
    Cython implementation of _MetaInfoInterface

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MetaInfoInterface.html>`_

    Interface for classes that can store arbitrary meta information
    (Type-Name-Value tuples).
    
    MetaInfoInterface is a base class for all classes that use one MetaInfo
    object as member.  If you want to add meta information to a class, let it
    publicly inherit the MetaInfoInterface.  Meta information is an array of
    Type-Name-Value tuples.
    
    Usage:
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MetaInfoInterface()
        """
        ...
    
    @overload
    def __init__(self, in_0: MetaInfoInterface ) -> None:
        """
        Cython signature: void MetaInfoInterface(MetaInfoInterface &)
        """
        ...
    
    def isMetaEmpty(self) -> bool:
        """
        Cython signature: bool isMetaEmpty()
        Returns if the MetaInfo is empty
        """
        ...
    
    def clearMetaInfo(self) -> None:
        """
        Cython signature: void clearMetaInfo()
        Removes all meta values
        """
        ...
    
    def metaRegistry(self) -> MetaInfoRegistry:
        """
        Cython signature: MetaInfoRegistry metaRegistry()
        Returns a reference to the MetaInfoRegistry
        """
        ...
    
    def getKeys(self, keys: List[bytes] ) -> None:
        """
        Cython signature: void getKeys(libcpp_vector[String] & keys)
        Fills the given vector with a list of all keys for which a value is set
        """
        ...
    
    def getMetaValue(self, in_0: Union[bytes, str, String] ) -> Union[int, float, bytes, str, List[int], List[float], List[bytes]]:
        """
        Cython signature: DataValue getMetaValue(String)
        Returns the value corresponding to a string, or
        """
        ...
    
    def setMetaValue(self, in_0: Union[bytes, str, String] , in_1: Union[int, float, bytes, str, List[int], List[float], List[bytes]] ) -> None:
        """
        Cython signature: void setMetaValue(String, DataValue)
        Sets the DataValue corresponding to a name
        """
        ...
    
    def metaValueExists(self, in_0: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool metaValueExists(String)
        Returns whether an entry with the given name exists
        """
        ...
    
    def removeMetaValue(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void removeMetaValue(String)
        Removes the DataValue corresponding to `name` if it exists
        """
        ...
    
    def __richcmp__(self, other: MetaInfoInterface, op: int) -> Any:
        ... 


class MetaboTargetedTargetDecoy:
    """
    Cython implementation of _MetaboTargetedTargetDecoy

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MetaboTargetedTargetDecoy.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MetaboTargetedTargetDecoy()
        Resolve overlapping fragments and missing decoys for experimental specific decoy generation in targeted/pseudo targeted metabolomics
        """
        ...
    
    @overload
    def __init__(self, in_0: MetaboTargetedTargetDecoy ) -> None:
        """
        Cython signature: void MetaboTargetedTargetDecoy(MetaboTargetedTargetDecoy &)
        """
        ...
    
    def constructTargetDecoyMassMapping(self, t_exp: TargetedExperiment ) -> List[MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping]:
        """
        Cython signature: libcpp_vector[MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping] constructTargetDecoyMassMapping(TargetedExperiment & t_exp)
        Constructs a mass mapping of targets and decoys using the unique m_id identifier
        
        
        :param t_exp: TransitionExperiment holds compound and transition information used for the mapping
        """
        ...
    
    def resolveOverlappingTargetDecoyMassesByIndividualMassShift(self, t_exp: TargetedExperiment , mappings: List[MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping] , mass_to_add: float ) -> None:
        """
        Cython signature: void resolveOverlappingTargetDecoyMassesByIndividualMassShift(TargetedExperiment & t_exp, libcpp_vector[MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping] & mappings, double & mass_to_add)
        Resolves overlapping target and decoy transition masses by adding a specifiable mass (e.g. CH2) to the overlapping decoy fragment
        
        
        :param t_exp: TransitionExperiment holds compound and transition information
        :param mappings: Map of identifier to target and decoy masses
        :param mass_to_add: (e.g. CH2)
        """
        ...
    
    def generateMissingDecoysByMassShift(self, t_exp: TargetedExperiment , mappings: List[MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping] , mass_to_add: float ) -> None:
        """
        Cython signature: void generateMissingDecoysByMassShift(TargetedExperiment & t_exp, libcpp_vector[MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping] & mappings, double & mass_to_add)
        Generate a decoy for targets where fragmentation tree re-rooting was not possible, by adding a specifiable mass to the target fragments
        
        
        :param t_exp: TransitionExperiment holds compound and transition information
        :param mappings: Map of identifier to target and decoy masses
        :param mass_to_add: The maximum number of transitions required per assay
        """
        ... 


class MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping:
    """
    Cython implementation of _MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping()
        """
        ...
    
    @overload
    def __init__(self, in_0: MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping ) -> None:
        """
        Cython signature: void MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping(MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping &)
        """
        ... 


class MzTabMFile:
    """
    Cython implementation of _MzTabMFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MzTabMFile.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MzTabMFile()
        """
        ...
    
    @overload
    def __init__(self, in_0: MzTabMFile ) -> None:
        """
        Cython signature: void MzTabMFile(MzTabMFile &)
        """
        ...
    
    def store(self, filename: Union[bytes, str, String] , mztab_m: MzTabM ) -> None:
        """
        Cython signature: void store(String filename, MzTabM & mztab_m)
        Store MzTabM file
        """
        ... 


class MzXMLFile:
    """
    Cython implementation of _MzXMLFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MzXMLFile.html>`_
      -- Inherits from ['ProgressLogger']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MzXMLFile()
        """
        ...
    
    @overload
    def __init__(self, in_0: MzXMLFile ) -> None:
        """
        Cython signature: void MzXMLFile(MzXMLFile &)
        """
        ...
    
    def load(self, filename: Union[bytes, str, String] , exp: MSExperiment ) -> None:
        """
        Cython signature: void load(String filename, MSExperiment & exp)
        Loads a MSExperiment from a MzXML file
        
        
        :param exp: MSExperiment
        """
        ...
    
    def store(self, filename: Union[bytes, str, String] , exp: MSExperiment ) -> None:
        """
        Cython signature: void store(String filename, MSExperiment & exp)
        Stores a MSExperiment in a MzXML file
        
        
        :param exp: MSExperiment
        """
        ...
    
    def getOptions(self) -> PeakFileOptions:
        """
        Cython signature: PeakFileOptions getOptions()
        Returns the options for loading/storing
        """
        ...
    
    def setOptions(self, in_0: PeakFileOptions ) -> None:
        """
        Cython signature: void setOptions(PeakFileOptions)
        Sets options for loading/storing
        """
        ...
    
    def setLogType(self, in_0: int ) -> None:
        """
        Cython signature: void setLogType(LogType)
        Sets the progress log that should be used. The default type is NONE!
        """
        ...
    
    def getLogType(self) -> int:
        """
        Cython signature: LogType getLogType()
        Returns the type of progress log being used
        """
        ...
    
    def startProgress(self, begin: int , end: int , label: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)
        """
        ...
    
    def setProgress(self, value: int ) -> None:
        """
        Cython signature: void setProgress(ptrdiff_t value)
        Sets the current progress
        """
        ...
    
    def endProgress(self) -> None:
        """
        Cython signature: void endProgress()
        Ends the progress display
        """
        ...
    
    def nextProgress(self) -> None:
        """
        Cython signature: void nextProgress()
        Increment progress by 1 (according to range begin-end)
        """
        ... 


class NeutralLossDiffFilter:
    """
    Cython implementation of _NeutralLossDiffFilter

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1NeutralLossDiffFilter.html>`_
      -- Inherits from ['FilterFunctor']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void NeutralLossDiffFilter()
        """
        ...
    
    @overload
    def __init__(self, in_0: NeutralLossDiffFilter ) -> None:
        """
        Cython signature: void NeutralLossDiffFilter(NeutralLossDiffFilter &)
        """
        ...
    
    def apply(self, in_0: MSSpectrum ) -> float:
        """
        Cython signature: double apply(MSSpectrum &)
        """
        ...
    
    def getProductName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getProductName()
        """
        ...
    
    def registerChildren(self) -> None:
        """
        Cython signature: void registerChildren()
        """
        ...
    
    def getSubsections(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getSubsections()
        """
        ...
    
    def setParameters(self, param: Param ) -> None:
        """
        Cython signature: void setParameters(Param & param)
        Sets the parameters
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        Returns the parameters
        """
        ...
    
    def getDefaults(self) -> Param:
        """
        Cython signature: Param getDefaults()
        Returns the default parameters
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name
        """
        ...
    
    def setName(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String &)
        Sets the name
        """
        ... 


class OMSSAXMLFile:
    """
    Cython implementation of _OMSSAXMLFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1OMSSAXMLFile.html>`_
      -- Inherits from ['XMLFile']
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void OMSSAXMLFile()
        """
        ...
    
    def load(self, filename: Union[bytes, str, String] , protein_identification: ProteinIdentification , id_data: List[PeptideIdentification] , load_proteins: bool , load_empty_hits: bool ) -> None:
        """
        Cython signature: void load(const String & filename, ProteinIdentification & protein_identification, libcpp_vector[PeptideIdentification] & id_data, bool load_proteins, bool load_empty_hits)
        Loads data from a OMSSAXML file
        
        
        :param filename: The file to be loaded
        :param protein_identification: Protein identifications belonging to the whole experiment
        :param id_data: The identifications with m/z and RT
        :param load_proteins: If this flag is set to false, the protein identifications are not loaded
        :param load_empty_hits: Many spectra will not return a hit. Report empty peptide identifications?
        """
        ...
    
    def setModificationDefinitionsSet(self, rhs: ModificationDefinitionsSet ) -> None:
        """
        Cython signature: void setModificationDefinitionsSet(ModificationDefinitionsSet rhs)
        Sets the valid modifications
        """
        ...
    
    def getVersion(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getVersion()
        Return the version of the schema
        """
        ... 


class OpenSwathScoring:
    """
    Cython implementation of _OpenSwathScoring

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1OpenSwathScoring.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void OpenSwathScoring()
        """
        ...
    
    @overload
    def __init__(self, in_0: OpenSwathScoring ) -> None:
        """
        Cython signature: void OpenSwathScoring(OpenSwathScoring &)
        """
        ...
    
    def initialize(self, rt_normalization_factor: float , add_up_spectra: int , spacing_for_spectra_resampling: float , drift_extra: float , su: OpenSwath_Scores_Usage , spectrum_addition_method: bytes ) -> None:
        """
        Cython signature: void initialize(double rt_normalization_factor, int add_up_spectra, double spacing_for_spectra_resampling, double drift_extra, OpenSwath_Scores_Usage su, libcpp_string spectrum_addition_method)
        Initialize the scoring object\n
        Sets the parameters for the scoring
        
        
        :param rt_normalization_factor: Specifies the range of the normalized retention time space
        :param add_up_spectra: How many spectra to add up (default 1)
        :param spacing_for_spectra_resampling: Spacing factor for spectra addition
        :param su: Which scores to actually compute
        :param spectrum_addition_method: Method to use for spectrum addition (valid: "simple", "resample")
        """
        ...
    
    def getNormalized_library_intensities_(self, transitions: List[LightTransition] , normalized_library_intensity: List[float] ) -> None:
        """
        Cython signature: void getNormalized_library_intensities_(libcpp_vector[LightTransition] transitions, libcpp_vector[double] normalized_library_intensity)
        """
        ... 


class OpenSwath_Scores:
    """
    Cython implementation of _OpenSwath_Scores

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1OpenSwath_Scores.html>`_
    """
    
    elution_model_fit_score: float
    
    library_corr: float
    
    library_norm_manhattan: float
    
    library_rootmeansquare: float
    
    library_sangle: float
    
    norm_rt_score: float
    
    isotope_correlation: float
    
    isotope_overlap: float
    
    massdev_score: float
    
    xcorr_coelution_score: float
    
    xcorr_shape_score: float
    
    yseries_score: float
    
    bseries_score: float
    
    log_sn_score: float
    
    weighted_coelution_score: float
    
    weighted_xcorr_shape: float
    
    weighted_massdev_score: float
    
    ms1_xcorr_coelution_score: float
    
    ms1_xcorr_coelution_contrast_score: float
    
    ms1_xcorr_coelution_combined_score: float
    
    ms1_xcorr_shape_score: float
    
    ms1_xcorr_shape_contrast_score: float
    
    ms1_xcorr_shape_combined_score: float
    
    ms1_ppm_score: float
    
    ms1_isotope_correlation: float
    
    ms1_isotope_overlap: float
    
    ms1_mi_score: float
    
    ms1_mi_contrast_score: float
    
    ms1_mi_combined_score: float
    
    sonar_sn: float
    
    sonar_diff: float
    
    sonar_trend: float
    
    sonar_rsq: float
    
    sonar_shape: float
    
    sonar_lag: float
    
    library_manhattan: float
    
    library_dotprod: float
    
    intensity: float
    
    total_xic: float
    
    nr_peaks: float
    
    sn_ratio: float
    
    mi_score: float
    
    weighted_mi_score: float
    
    rt_difference: float
    
    normalized_experimental_rt: float
    
    raw_rt_score: float
    
    dotprod_score_dia: float
    
    manhatt_score_dia: float
    
    def __init__(self) -> None:
        """
        Cython signature: void OpenSwath_Scores()
        """
        ...
    
    def get_quick_lda_score(self, library_corr_: float , library_norm_manhattan_: float , norm_rt_score_: float , xcorr_coelution_score_: float , xcorr_shape_score_: float , log_sn_score_: float ) -> float:
        """
        Cython signature: double get_quick_lda_score(double library_corr_, double library_norm_manhattan_, double norm_rt_score_, double xcorr_coelution_score_, double xcorr_shape_score_, double log_sn_score_)
        """
        ...
    
    def calculate_lda_prescore(self, scores: OpenSwath_Scores ) -> float:
        """
        Cython signature: double calculate_lda_prescore(OpenSwath_Scores scores)
        """
        ...
    
    def calculate_swath_lda_prescore(self, scores: OpenSwath_Scores ) -> float:
        """
        Cython signature: double calculate_swath_lda_prescore(OpenSwath_Scores scores)
        """
        ... 


class OpenSwath_Scores_Usage:
    """
    Cython implementation of _OpenSwath_Scores_Usage

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1OpenSwath_Scores_Usage.html>`_
    """
    
    use_coelution_score_: bool
    
    use_shape_score_: bool
    
    use_rt_score_: bool
    
    use_library_score_: bool
    
    use_elution_model_score_: bool
    
    use_intensity_score_: bool
    
    use_total_xic_score_: bool
    
    use_total_mi_score_: bool
    
    use_nr_peaks_score_: bool
    
    use_sn_score_: bool
    
    use_mi_score_: bool
    
    use_dia_scores_: bool
    
    use_sonar_scores: bool
    
    use_ms1_correlation: bool
    
    use_ms1_fullscan: bool
    
    use_ms1_mi: bool
    
    use_uis_scores: bool
    
    def __init__(self) -> None:
        """
        Cython signature: void OpenSwath_Scores_Usage()
        """
        ... 


class ParentPeakMower:
    """
    Cython implementation of _ParentPeakMower

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ParentPeakMower.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ParentPeakMower()
        """
        ...
    
    @overload
    def __init__(self, in_0: ParentPeakMower ) -> None:
        """
        Cython signature: void ParentPeakMower(ParentPeakMower &)
        """
        ...
    
    def filterSpectrum(self, spec: MSSpectrum ) -> None:
        """
        Cython signature: void filterSpectrum(MSSpectrum & spec)
        """
        ...
    
    def filterPeakSpectrum(self, spec: MSSpectrum ) -> None:
        """
        Cython signature: void filterPeakSpectrum(MSSpectrum & spec)
        """
        ...
    
    def filterPeakMap(self, exp: MSExperiment ) -> None:
        """
        Cython signature: void filterPeakMap(MSExperiment & exp)
        """
        ...
    
    def getSubsections(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getSubsections()
        """
        ...
    
    def setParameters(self, param: Param ) -> None:
        """
        Cython signature: void setParameters(Param & param)
        Sets the parameters
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        Returns the parameters
        """
        ...
    
    def getDefaults(self) -> Param:
        """
        Cython signature: Param getDefaults()
        Returns the default parameters
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name
        """
        ...
    
    def setName(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String &)
        Sets the name
        """
        ... 


class PeakBoundary:
    """
    Cython implementation of _PeakBoundary

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakBoundary.html>`_
    """
    
    mz_min: float
    
    mz_max: float
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void PeakBoundary()
        """
        ...
    
    @overload
    def __init__(self, in_0: PeakBoundary ) -> None:
        """
        Cython signature: void PeakBoundary(PeakBoundary &)
        """
        ... 


class PeakPickerHiRes:
    """
    Cython implementation of _PeakPickerHiRes

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakPickerHiRes.html>`_
      -- Inherits from ['DefaultParamHandler', 'ProgressLogger']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void PeakPickerHiRes()
        """
        ...
    
    @overload
    def __init__(self, in_0: PeakPickerHiRes ) -> None:
        """
        Cython signature: void PeakPickerHiRes(PeakPickerHiRes &)
        """
        ...
    
    @overload
    def pick(self, input: MSSpectrum , output: MSSpectrum ) -> None:
        """
        Cython signature: void pick(MSSpectrum & input, MSSpectrum & output)
        """
        ...
    
    @overload
    def pick(self, input: MSChromatogram , output: MSChromatogram ) -> None:
        """
        Cython signature: void pick(MSChromatogram & input, MSChromatogram & output)
        """
        ...
    
    @overload
    def pickExperiment(self, input: MSExperiment , output: MSExperiment , check_spectrum_type: bool ) -> None:
        """
        Cython signature: void pickExperiment(MSExperiment & input, MSExperiment & output, bool check_spectrum_type)
        Applies the peak-picking algorithm to a map (MSExperiment). This method picks peaks for each scan in the map consecutively. The resulting
        picked peaks are written to the output map
        
        
        :param input: Input map in profile mode
        :param output: Output map with picked peaks
        :param check_spectrum_type: If set, checks spectrum type and throws an exception if a centroided spectrum is passed
        """
        ...
    
    @overload
    def pickExperiment(self, input: MSExperiment , output: MSExperiment , boundaries_spec: List[List[PeakBoundary]] , boundaries_chrom: List[List[PeakBoundary]] , check_spectrum_type: bool ) -> None:
        """
        Cython signature: void pickExperiment(MSExperiment & input, MSExperiment & output, libcpp_vector[libcpp_vector[PeakBoundary]] & boundaries_spec, libcpp_vector[libcpp_vector[PeakBoundary]] & boundaries_chrom, bool check_spectrum_type)
        """
        ...
    
    def getSubsections(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getSubsections()
        """
        ...
    
    def setParameters(self, param: Param ) -> None:
        """
        Cython signature: void setParameters(Param & param)
        Sets the parameters
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        Returns the parameters
        """
        ...
    
    def getDefaults(self) -> Param:
        """
        Cython signature: Param getDefaults()
        Returns the default parameters
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name
        """
        ...
    
    def setName(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String &)
        Sets the name
        """
        ...
    
    def setLogType(self, in_0: int ) -> None:
        """
        Cython signature: void setLogType(LogType)
        Sets the progress log that should be used. The default type is NONE!
        """
        ...
    
    def getLogType(self) -> int:
        """
        Cython signature: LogType getLogType()
        Returns the type of progress log being used
        """
        ...
    
    def startProgress(self, begin: int , end: int , label: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)
        """
        ...
    
    def setProgress(self, value: int ) -> None:
        """
        Cython signature: void setProgress(ptrdiff_t value)
        Sets the current progress
        """
        ...
    
    def endProgress(self) -> None:
        """
        Cython signature: void endProgress()
        Ends the progress display
        """
        ...
    
    def nextProgress(self) -> None:
        """
        Cython signature: void nextProgress()
        Increment progress by 1 (according to range begin-end)
        """
        ... 


class PeptideAndProteinQuant:
    """
    Cython implementation of _PeptideAndProteinQuant

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeptideAndProteinQuant.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void PeptideAndProteinQuant()
        Helper class for peptide and protein quantification based on feature data annotated with IDs
        """
        ...
    
    @overload
    def __init__(self, in_0: PeptideAndProteinQuant ) -> None:
        """
        Cython signature: void PeptideAndProteinQuant(PeptideAndProteinQuant &)
        """
        ...
    
    @overload
    def readQuantData(self, map_in: FeatureMap , ed: ExperimentalDesign ) -> None:
        """
        Cython signature: void readQuantData(FeatureMap & map_in, ExperimentalDesign & ed)
        Read quantitative data from a feature map
        
        Parameters should be set before using this method, as setting parameters will clear all results
        """
        ...
    
    @overload
    def readQuantData(self, map_in: ConsensusMap , ed: ExperimentalDesign ) -> None:
        """
        Cython signature: void readQuantData(ConsensusMap & map_in, ExperimentalDesign & ed)
        Read quantitative data from a consensus map
        
        Parameters should be set before using this method, as setting parameters will clear all results
        """
        ...
    
    @overload
    def readQuantData(self, proteins: List[ProteinIdentification] , peptides: List[PeptideIdentification] , ed: ExperimentalDesign ) -> None:
        """
        Cython signature: void readQuantData(libcpp_vector[ProteinIdentification] & proteins, libcpp_vector[PeptideIdentification] & peptides, ExperimentalDesign & ed)
        Read quantitative data from identification results (for quantification via spectral counting)
        
        Parameters should be set before using this method, as setting parameters will clear all results
        """
        ...
    
    def quantifyPeptides(self, peptides: List[PeptideIdentification] ) -> None:
        """
        Cython signature: void quantifyPeptides(libcpp_vector[PeptideIdentification] & peptides)
        Compute peptide abundances
        
        Based on quantitative data for individual charge states (in member `pep_quant_`), overall abundances for peptides are computed (and stored again in `pep_quant_`)
        Quantitative data must first be read via readQuantData()
        Optional (peptide-level) protein inference information (e.g. from Fido or ProteinProphet) can be supplied via `peptides`. In that case, peptide-to-protein associations - the basis for protein-level quantification - will also be read from `peptides`!
        """
        ...
    
    def quantifyProteins(self, proteins: ProteinIdentification ) -> None:
        """
        Cython signature: void quantifyProteins(ProteinIdentification & proteins)
        Compute protein abundances
        
        Peptide abundances must be computed first with quantifyPeptides(). Optional protein inference information (e.g. from Fido or ProteinProphet) can be supplied via `proteins`
        """
        ...
    
    def getStatistics(self) -> PeptideAndProteinQuant_Statistics:
        """
        Cython signature: PeptideAndProteinQuant_Statistics getStatistics()
        """
        ...
    
    def getSubsections(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getSubsections()
        """
        ...
    
    def setParameters(self, param: Param ) -> None:
        """
        Cython signature: void setParameters(Param & param)
        Sets the parameters
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        Returns the parameters
        """
        ...
    
    def getDefaults(self) -> Param:
        """
        Cython signature: Param getDefaults()
        Returns the default parameters
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name
        """
        ...
    
    def setName(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String &)
        Sets the name
        """
        ... 


class PeptideAndProteinQuant_PeptideData:
    """
    Cython implementation of _PeptideAndProteinQuant_PeptideData

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeptideAndProteinQuant_PeptideData.html>`_
    """
    
    accessions: Set[bytes]
    
    psm_count: int
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void PeptideAndProteinQuant_PeptideData()
        """
        ...
    
    @overload
    def __init__(self, in_0: PeptideAndProteinQuant_PeptideData ) -> None:
        """
        Cython signature: void PeptideAndProteinQuant_PeptideData(PeptideAndProteinQuant_PeptideData &)
        """
        ... 


class PeptideAndProteinQuant_ProteinData:
    """
    Cython implementation of _PeptideAndProteinQuant_ProteinData

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeptideAndProteinQuant_ProteinData.html>`_
    """
    
    psm_count: int
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void PeptideAndProteinQuant_ProteinData()
        """
        ...
    
    @overload
    def __init__(self, in_0: PeptideAndProteinQuant_ProteinData ) -> None:
        """
        Cython signature: void PeptideAndProteinQuant_ProteinData(PeptideAndProteinQuant_ProteinData &)
        """
        ... 


class PeptideAndProteinQuant_Statistics:
    """
    Cython implementation of _PeptideAndProteinQuant_Statistics

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeptideAndProteinQuant_Statistics.html>`_
    """
    
    n_samples: int
    
    quant_proteins: int
    
    too_few_peptides: int
    
    quant_peptides: int
    
    total_peptides: int
    
    quant_features: int
    
    total_features: int
    
    blank_features: int
    
    ambig_features: int
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void PeptideAndProteinQuant_Statistics()
        """
        ...
    
    @overload
    def __init__(self, in_0: PeptideAndProteinQuant_Statistics ) -> None:
        """
        Cython signature: void PeptideAndProteinQuant_Statistics(PeptideAndProteinQuant_Statistics &)
        """
        ... 


class PrecursorCorrection:
    """
    Cython implementation of _PrecursorCorrection

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PrecursorCorrection.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void PrecursorCorrection()
        """
        ...
    
    @overload
    def __init__(self, in_0: PrecursorCorrection ) -> None:
        """
        Cython signature: void PrecursorCorrection(PrecursorCorrection &)
        """
        ...
    
    correctToHighestIntensityMS1Peak: __static_PrecursorCorrection_correctToHighestIntensityMS1Peak
    
    correctToNearestFeature: __static_PrecursorCorrection_correctToNearestFeature
    
    correctToNearestMS1Peak: __static_PrecursorCorrection_correctToNearestMS1Peak
    
    getPrecursors: __static_PrecursorCorrection_getPrecursors
    
    writeHist: __static_PrecursorCorrection_writeHist 


class PrecursorPurity:
    """
    Cython implementation of _PrecursorPurity

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PrecursorPurity.html>`_

    Precursor purity or noise estimation
    
    This class computes metrics for precursor isolation window purity (or noise)
    The function extracts the peaks from an isolation window targeted for fragmentation
    and determines which peaks are isotopes of the target and which come from other sources
    The intensities of the assumed target peaks are summed up as the target intensity
    Using this information it calculates an intensity ratio for the relative intensity of the target
    compared to other sources
    These metrics are combined over the previous and the next MS1 spectrum
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void PrecursorPurity()
        """
        ...
    
    @overload
    def __init__(self, in_0: PrecursorPurity ) -> None:
        """
        Cython signature: void PrecursorPurity(PrecursorPurity &)
        """
        ...
    
    def computePrecursorPurity(self, ms1: MSSpectrum , pre: Precursor , precursor_mass_tolerance: float , precursor_mass_tolerance_unit_ppm: bool ) -> PurityScores:
        """
        Cython signature: PurityScores computePrecursorPurity(MSSpectrum ms1, Precursor pre, double precursor_mass_tolerance, bool precursor_mass_tolerance_unit_ppm)
        Compute precursor purity metrics for one MS2 precursor
        
        Note: This function is implemented in a general way and can also be used for e.g. MS3 precursor isolation windows in MS2 spectra
        Spectra annotated with charge 0 will be treated as charge 1.
        
        
        :param ms1: The Spectrum containing the isolation window
        :param pre: The precursor containing the definition the isolation window
        :param precursor_mass_tolerance: The precursor tolerance. Is used for determining the targeted peak and deisotoping
        :param precursor_mass_tolerance_unit_ppm: The unit of the precursor tolerance
        """
        ... 


class PurityScores:
    """
    Cython implementation of _PurityScores

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PurityScores.html>`_
    """
    
    total_intensity: float
    
    target_intensity: float
    
    signal_proportion: float
    
    target_peak_count: int
    
    residual_peak_count: int
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void PurityScores()
        """
        ...
    
    @overload
    def __init__(self, in_0: PurityScores ) -> None:
        """
        Cython signature: void PurityScores(PurityScores &)
        """
        ... 


class QuantitativeExperimentalDesign:
    """
    Cython implementation of _QuantitativeExperimentalDesign

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1QuantitativeExperimentalDesign.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void QuantitativeExperimentalDesign()
        """
        ...
    
    def applyDesign2Resolver(self, resolver: ProteinResolver , file_: TextFile , fileNames: List[bytes] ) -> None:
        """
        Cython signature: void applyDesign2Resolver(ProteinResolver & resolver, TextFile & file_, StringList & fileNames)
        """
        ...
    
    def getSubsections(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getSubsections()
        """
        ...
    
    def setParameters(self, param: Param ) -> None:
        """
        Cython signature: void setParameters(Param & param)
        Sets the parameters
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        Returns the parameters
        """
        ...
    
    def getDefaults(self) -> Param:
        """
        Cython signature: Param getDefaults()
        Returns the default parameters
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name
        """
        ...
    
    def setName(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String &)
        Sets the name
        """
        ... 


class RNPxlMarkerIonExtractor:
    """
    Cython implementation of _RNPxlMarkerIonExtractor

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1RNPxlMarkerIonExtractor.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void RNPxlMarkerIonExtractor()
        """
        ...
    
    @overload
    def __init__(self, in_0: RNPxlMarkerIonExtractor ) -> None:
        """
        Cython signature: void RNPxlMarkerIonExtractor(RNPxlMarkerIonExtractor &)
        """
        ...
    
    def extractMarkerIons(self, s: MSSpectrum , marker_tolerance: float ) -> Dict[Union[bytes, str, String], List[List[float, float]]]:
        """
        Cython signature: libcpp_map[String,libcpp_vector[libcpp_pair[double,double]]] extractMarkerIons(MSSpectrum & s, double marker_tolerance)
        """
        ... 


class RNaseDB:
    """
    Cython implementation of _RNaseDB

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1RNaseDB.html>`_
    """
    
    def getEnzyme(self, name: Union[bytes, str, String] ) -> DigestionEnzymeRNA:
        """
        Cython signature: const DigestionEnzymeRNA * getEnzyme(const String & name)
        """
        ...
    
    def getEnzymeByRegEx(self, cleavage_regex: Union[bytes, str, String] ) -> DigestionEnzymeRNA:
        """
        Cython signature: const DigestionEnzymeRNA * getEnzymeByRegEx(const String & cleavage_regex)
        """
        ...
    
    def getAllNames(self, all_names: List[bytes] ) -> None:
        """
        Cython signature: void getAllNames(libcpp_vector[String] & all_names)
        """
        ...
    
    def hasEnzyme(self, name: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool hasEnzyme(const String & name)
        """
        ...
    
    def hasRegEx(self, cleavage_regex: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool hasRegEx(const String & cleavage_regex)
        """
        ... 


class Ribonucleotide:
    """
    Cython implementation of _Ribonucleotide

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::Ribonucleotide_1_1Ribonucleotide.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void Ribonucleotide()
        """
        ...
    
    @overload
    def __init__(self, in_0: Ribonucleotide ) -> None:
        """
        Cython signature: void Ribonucleotide(Ribonucleotide &)
        """
        ...
    
    @overload
    def __init__(self, name: Union[bytes, str, String] , code: Union[bytes, str, String] , new_code: Union[bytes, str, String] , html_code: Union[bytes, str, String] , formula: EmpiricalFormula , origin: bytes , mono_mass: float , avg_mass: float , term_spec: int , baseloss_formula: EmpiricalFormula ) -> None:
        """
        Cython signature: void Ribonucleotide(String name, String code, String new_code, String html_code, EmpiricalFormula formula, char origin, double mono_mass, double avg_mass, TermSpecificityNuc term_spec, EmpiricalFormula baseloss_formula)
        """
        ...
    
    def getCode(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getCode()
        Returns the short name
        """
        ...
    
    def setCode(self, code: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setCode(String code)
        Sets the short name
        """
        ...
    
    def setName(self, name: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(String name)
        Sets the name of the ribonucleotide
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name of the ribonucleotide
        """
        ...
    
    def setFormula(self, formula: EmpiricalFormula ) -> None:
        """
        Cython signature: void setFormula(EmpiricalFormula formula)
        Sets empirical formula of the ribonucleotide (must be full, with N and C-terminus)
        """
        ...
    
    def getFormula(self) -> EmpiricalFormula:
        """
        Cython signature: EmpiricalFormula getFormula()
        Returns the empirical formula of the residue
        """
        ...
    
    def setAvgMass(self, avg_mass: float ) -> None:
        """
        Cython signature: void setAvgMass(double avg_mass)
        Sets average mass of the ribonucleotide
        """
        ...
    
    def getAvgMass(self) -> float:
        """
        Cython signature: double getAvgMass()
        Returns average mass of the ribonucleotide
        """
        ...
    
    def setMonoMass(self, mono_mass: float ) -> None:
        """
        Cython signature: void setMonoMass(double mono_mass)
        Sets monoisotopic mass of the ribonucleotide
        """
        ...
    
    def getMonoMass(self) -> float:
        """
        Cython signature: double getMonoMass()
        Returns monoisotopic mass of the ribonucleotide
        """
        ...
    
    def getNewCode(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getNewCode()
        Returns the new code
        """
        ...
    
    def setNewCode(self, code: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setNewCode(String code)
        Sets the new code
        """
        ...
    
    def getOrigin(self) -> bytes:
        """
        Cython signature: char getOrigin()
        Returns the code of the unmodified base (e.g., "A", "C", ...)
        """
        ...
    
    def setOrigin(self, origin: bytes ) -> None:
        """
        Cython signature: void setOrigin(char origin)
        Sets the code of the unmodified base (e.g., "A", "C", ...)
        """
        ...
    
    def setHTMLCode(self, html_code: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setHTMLCode(String html_code)
        Sets the HTML (RNAMods) code
        """
        ...
    
    def getHTMLCode(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getHTMLCode()
        Returns the HTML (RNAMods) code
        """
        ...
    
    def setTermSpecificity(self, term_spec: int ) -> None:
        """
        Cython signature: void setTermSpecificity(TermSpecificityNuc term_spec)
        Sets the terminal specificity
        """
        ...
    
    def getTermSpecificity(self) -> int:
        """
        Cython signature: TermSpecificityNuc getTermSpecificity()
        Returns the terminal specificity
        """
        ...
    
    def getBaselossFormula(self) -> EmpiricalFormula:
        """
        Cython signature: EmpiricalFormula getBaselossFormula()
        Returns sum formula after loss of the nucleobase
        """
        ...
    
    def setBaselossFormula(self, formula: EmpiricalFormula ) -> None:
        """
        Cython signature: void setBaselossFormula(EmpiricalFormula formula)
        Sets sum formula after loss of the nucleobase
        """
        ...
    
    def isModified(self) -> bool:
        """
        Cython signature: bool isModified()
        True if the ribonucleotide is a modified one
        """
        ...
    
    def __richcmp__(self, other: Ribonucleotide, op: int) -> Any:
        ... 


class RichPeak2D:
    """
    Cython implementation of _RichPeak2D

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1RichPeak2D.html>`_
      -- Inherits from ['Peak2D', 'UniqueIdInterface', 'MetaInfoInterface']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void RichPeak2D()
        A 2-dimensional raw data point or peak with meta information
        """
        ...
    
    @overload
    def __init__(self, in_0: RichPeak2D ) -> None:
        """
        Cython signature: void RichPeak2D(RichPeak2D &)
        """
        ...
    
    def getIntensity(self) -> float:
        """
        Cython signature: float getIntensity()
        Returns the data point intensity (height)
        """
        ...
    
    def getMZ(self) -> float:
        """
        Cython signature: double getMZ()
        Returns the m/z coordinate (index 1)
        """
        ...
    
    def getRT(self) -> float:
        """
        Cython signature: double getRT()
        Returns the RT coordinate (index 0)
        """
        ...
    
    def setMZ(self, in_0: float ) -> None:
        """
        Cython signature: void setMZ(double)
        Returns the m/z coordinate (index 1)
        """
        ...
    
    def setRT(self, in_0: float ) -> None:
        """
        Cython signature: void setRT(double)
        Returns the RT coordinate (index 0)
        """
        ...
    
    def setIntensity(self, in_0: float ) -> None:
        """
        Cython signature: void setIntensity(float)
        Returns the data point intensity (height)
        """
        ...
    
    def getUniqueId(self) -> int:
        """
        Cython signature: size_t getUniqueId()
        Returns the unique id
        """
        ...
    
    def clearUniqueId(self) -> int:
        """
        Cython signature: size_t clearUniqueId()
        Clear the unique id. The new unique id will be invalid. Returns 1 if the unique id was changed, 0 otherwise
        """
        ...
    
    def hasValidUniqueId(self) -> int:
        """
        Cython signature: size_t hasValidUniqueId()
        Returns whether the unique id is valid. Returns 1 if the unique id is valid, 0 otherwise
        """
        ...
    
    def hasInvalidUniqueId(self) -> int:
        """
        Cython signature: size_t hasInvalidUniqueId()
        Returns whether the unique id is invalid. Returns 1 if the unique id is invalid, 0 otherwise
        """
        ...
    
    def setUniqueId(self, rhs: int ) -> None:
        """
        Cython signature: void setUniqueId(uint64_t rhs)
        Assigns a new, valid unique id. Always returns 1
        """
        ...
    
    def ensureUniqueId(self) -> int:
        """
        Cython signature: size_t ensureUniqueId()
        Assigns a valid unique id, but only if the present one is invalid. Returns 1 if the unique id was changed, 0 otherwise
        """
        ...
    
    def isValid(self, unique_id: int ) -> bool:
        """
        Cython signature: bool isValid(uint64_t unique_id)
        Returns true if the unique_id is valid, false otherwise
        """
        ...
    
    def isMetaEmpty(self) -> bool:
        """
        Cython signature: bool isMetaEmpty()
        Returns if the MetaInfo is empty
        """
        ...
    
    def clearMetaInfo(self) -> None:
        """
        Cython signature: void clearMetaInfo()
        Removes all meta values
        """
        ...
    
    def metaRegistry(self) -> MetaInfoRegistry:
        """
        Cython signature: MetaInfoRegistry metaRegistry()
        Returns a reference to the MetaInfoRegistry
        """
        ...
    
    def getKeys(self, keys: List[bytes] ) -> None:
        """
        Cython signature: void getKeys(libcpp_vector[String] & keys)
        Fills the given vector with a list of all keys for which a value is set
        """
        ...
    
    def getMetaValue(self, in_0: Union[bytes, str, String] ) -> Union[int, float, bytes, str, List[int], List[float], List[bytes]]:
        """
        Cython signature: DataValue getMetaValue(String)
        Returns the value corresponding to a string, or
        """
        ...
    
    def setMetaValue(self, in_0: Union[bytes, str, String] , in_1: Union[int, float, bytes, str, List[int], List[float], List[bytes]] ) -> None:
        """
        Cython signature: void setMetaValue(String, DataValue)
        Sets the DataValue corresponding to a name
        """
        ...
    
    def metaValueExists(self, in_0: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool metaValueExists(String)
        Returns whether an entry with the given name exists
        """
        ...
    
    def removeMetaValue(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void removeMetaValue(String)
        Removes the DataValue corresponding to `name` if it exists
        """
        ...
    
    def __richcmp__(self, other: RichPeak2D, op: int) -> Any:
        ... 


class ScanWindow:
    """
    Cython implementation of _ScanWindow

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ScanWindow.html>`_
      -- Inherits from ['MetaInfoInterface']
    """
    
    begin: float
    
    end: float
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ScanWindow()
        """
        ...
    
    @overload
    def __init__(self, in_0: ScanWindow ) -> None:
        """
        Cython signature: void ScanWindow(ScanWindow &)
        """
        ...
    
    def isMetaEmpty(self) -> bool:
        """
        Cython signature: bool isMetaEmpty()
        Returns if the MetaInfo is empty
        """
        ...
    
    def clearMetaInfo(self) -> None:
        """
        Cython signature: void clearMetaInfo()
        Removes all meta values
        """
        ...
    
    def metaRegistry(self) -> MetaInfoRegistry:
        """
        Cython signature: MetaInfoRegistry metaRegistry()
        Returns a reference to the MetaInfoRegistry
        """
        ...
    
    def getKeys(self, keys: List[bytes] ) -> None:
        """
        Cython signature: void getKeys(libcpp_vector[String] & keys)
        Fills the given vector with a list of all keys for which a value is set
        """
        ...
    
    def getMetaValue(self, in_0: Union[bytes, str, String] ) -> Union[int, float, bytes, str, List[int], List[float], List[bytes]]:
        """
        Cython signature: DataValue getMetaValue(String)
        Returns the value corresponding to a string, or
        """
        ...
    
    def setMetaValue(self, in_0: Union[bytes, str, String] , in_1: Union[int, float, bytes, str, List[int], List[float], List[bytes]] ) -> None:
        """
        Cython signature: void setMetaValue(String, DataValue)
        Sets the DataValue corresponding to a name
        """
        ...
    
    def metaValueExists(self, in_0: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool metaValueExists(String)
        Returns whether an entry with the given name exists
        """
        ...
    
    def removeMetaValue(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void removeMetaValue(String)
        Removes the DataValue corresponding to `name` if it exists
        """
        ...
    
    def __richcmp__(self, other: ScanWindow, op: int) -> Any:
        ... 


class Seed:
    """
    Cython implementation of _Seed

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::FeatureFinderAlgorithmPickedHelperStructs_1_1Seed.html>`_
    """
    
    spectrum: int
    
    peak: int
    
    intensity: float
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void Seed()
        """
        ...
    
    @overload
    def __init__(self, in_0: Seed ) -> None:
        """
        Cython signature: void Seed(Seed &)
        """
        ...
    
    def __richcmp__(self, other: Seed, op: int) -> Any:
        ... 


class SequestInfile:
    """
    Cython implementation of _SequestInfile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1SequestInfile.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void SequestInfile()
        Sequest input file adapter
        """
        ...
    
    @overload
    def __init__(self, in_0: SequestInfile ) -> None:
        """
        Cython signature: void SequestInfile(SequestInfile &)
        """
        ...
    
    def store(self, filename: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void store(const String & filename)
        Stores the experiment data in a Sequest input file that can be used as input for Sequest shell execution
        
        :param filename: the name of the file in which the infile is stored into
        """
        ...
    
    def getEnzymeInfoAsString(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getEnzymeInfoAsString()
        Returns the enzyme list as a string
        """
        ...
    
    def getDatabase(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getDatabase()
        Returns the used database
        """
        ...
    
    def setDatabase(self, database: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setDatabase(const String & database)
        Sets the used database
        """
        ...
    
    def getNeutralLossesForIons(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getNeutralLossesForIons()
        Returns whether neutral losses are considered for the a-, b- and y-ions
        """
        ...
    
    def setNeutralLossesForIons(self, neutral_losses_for_ions: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setNeutralLossesForIons(const String & neutral_losses_for_ions)
        Sets whether neutral losses are considered for the a-, b- and y-ions
        """
        ...
    
    def getIonSeriesWeights(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getIonSeriesWeights()
        Returns the weights for the a-, b-, c-, d-, v-, w-, x-, y- and z-ion series
        """
        ...
    
    def setIonSeriesWeights(self, ion_series_weights: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setIonSeriesWeights(const String & ion_series_weights)
        Sets the weights for the a-, b-, c-, d-, v-, w-, x-, y- and z-ion series
        """
        ...
    
    def getPartialSequence(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getPartialSequence()
        Returns the partial sequences (space delimited) that have to occur in the theoretical spectra
        """
        ...
    
    def setPartialSequence(self, partial_sequence: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setPartialSequence(const String & partial_sequence)
        Sets the partial sequences (space delimited) that have to occur in the theoretical spectra
        """
        ...
    
    def getSequenceHeaderFilter(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getSequenceHeaderFilter()
        Returns the sequences (space delimited) that have to occur, or be absent (preceded by a tilde) in the header of a protein to be considered
        """
        ...
    
    def setSequenceHeaderFilter(self, sequence_header_filter: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setSequenceHeaderFilter(const String & sequence_header_filter)
        Sets the sequences (space delimited) that have to occur, or be absent (preceded by a tilde) in the header of a protein to be considered
        """
        ...
    
    def getProteinMassFilter(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getProteinMassFilter()
        Returns the protein mass filter (either min and max mass, or mass and tolerance value in percent)
        """
        ...
    
    def setProteinMassFilter(self, protein_mass_filter: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setProteinMassFilter(const String & protein_mass_filter)
        Sets the protein mass filter (either min and max mass, or mass and tolerance value in percent)
        """
        ...
    
    def getPeakMassTolerance(self) -> float:
        """
        Cython signature: float getPeakMassTolerance()
        Returns the peak mass tolerance
        """
        ...
    
    def setPeakMassTolerance(self, peak_mass_tolerance: float ) -> None:
        """
        Cython signature: void setPeakMassTolerance(float peak_mass_tolerance)
        Sets the peak mass tolerance
        """
        ...
    
    def getPrecursorMassTolerance(self) -> float:
        """
        Cython signature: float getPrecursorMassTolerance()
        Returns the precursor mass tolerance
        """
        ...
    
    def setPrecursorMassTolerance(self, precursor_mass_tolerance: float ) -> None:
        """
        Cython signature: void setPrecursorMassTolerance(float precursor_mass_tolerance)
        Sets the precursor mass tolerance
        """
        ...
    
    def getMatchPeakTolerance(self) -> float:
        """
        Cython signature: float getMatchPeakTolerance()
        Returns the match peak tolerance
        """
        ...
    
    def setMatchPeakTolerance(self, match_peak_tolerance: float ) -> None:
        """
        Cython signature: void setMatchPeakTolerance(float match_peak_tolerance)
        Sets the match peak tolerance
        """
        ...
    
    def getIonCutoffPercentage(self) -> float:
        """
        Cython signature: float getIonCutoffPercentage()
        Returns the the cutoff of the ratio matching theoretical peaks/theoretical peaks
        """
        ...
    
    def setIonCutoffPercentage(self, ion_cutoff_percentage: float ) -> None:
        """
        Cython signature: void setIonCutoffPercentage(float ion_cutoff_percentage)
        Sets the ion cutoff of the ratio matching theoretical peaks/theoretical peaks
        """
        ...
    
    def getPeptideMassUnit(self) -> int:
        """
        Cython signature: size_t getPeptideMassUnit()
        Returns the peptide mass unit
        """
        ...
    
    def setPeptideMassUnit(self, peptide_mass_unit: int ) -> None:
        """
        Cython signature: void setPeptideMassUnit(size_t peptide_mass_unit)
        Sets the peptide mass unit
        """
        ...
    
    def getOutputLines(self) -> int:
        """
        Cython signature: size_t getOutputLines()
        Returns the number of peptides to be displayed
        """
        ...
    
    def setOutputLines(self, output_lines: int ) -> None:
        """
        Cython signature: void setOutputLines(size_t output_lines)
        Sets the number of peptides to be displayed
        """
        ...
    
    def getEnzymeNumber(self) -> int:
        """
        Cython signature: size_t getEnzymeNumber()
        Returns the enzyme used for cleavage (by means of the number from a list of enzymes)
        """
        ...
    
    def getEnzymeName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getEnzymeName()
        Returns the enzyme used for cleavage
        """
        ...
    
    def setEnzyme(self, enzyme_name: Union[bytes, str, String] ) -> int:
        """
        Cython signature: size_t setEnzyme(String enzyme_name)
        Sets the enzyme used for cleavage (by means of the number from a list of enzymes)
        """
        ...
    
    def getMaxAAPerModPerPeptide(self) -> int:
        """
        Cython signature: size_t getMaxAAPerModPerPeptide()
        Returns the maximum number of amino acids containing the same modification in a peptide
        """
        ...
    
    def setMaxAAPerModPerPeptide(self, max_aa_per_mod_per_peptide: int ) -> None:
        """
        Cython signature: void setMaxAAPerModPerPeptide(size_t max_aa_per_mod_per_peptide)
        Sets the maximum number of amino acids containing the same modification in a peptide
        """
        ...
    
    def getMaxModsPerPeptide(self) -> int:
        """
        Cython signature: size_t getMaxModsPerPeptide()
        Returns the maximum number of modifications that are allowed in a peptide
        """
        ...
    
    def setMaxModsPerPeptide(self, max_mods_per_peptide: int ) -> None:
        """
        Cython signature: void setMaxModsPerPeptide(size_t max_mods_per_peptide)
        Sets the maximum number of modifications that are allowed in a peptide
        """
        ...
    
    def getNucleotideReadingFrame(self) -> int:
        """
        Cython signature: size_t getNucleotideReadingFrame()
        Returns the nucleotide reading frame
        """
        ...
    
    def setNucleotideReadingFrame(self, nucleotide_reading_frame: int ) -> None:
        """
        Cython signature: void setNucleotideReadingFrame(size_t nucleotide_reading_frame)
        Sets the nucleotide reading frame
        """
        ...
    
    def getMaxInternalCleavageSites(self) -> int:
        """
        Cython signature: size_t getMaxInternalCleavageSites()
        Returns the maximum number of internal cleavage sites
        """
        ...
    
    def setMaxInternalCleavageSites(self, max_internal_cleavage_sites: int ) -> None:
        """
        Cython signature: void setMaxInternalCleavageSites(size_t max_internal_cleavage_sites)
        Sets the maximum number of internal cleavage sites
        """
        ...
    
    def getMatchPeakCount(self) -> int:
        """
        Cython signature: size_t getMatchPeakCount()
        Returns the number of top abundant peaks to match with theoretical ones
        """
        ...
    
    def setMatchPeakCount(self, match_peak_count: int ) -> None:
        """
        Cython signature: void setMatchPeakCount(size_t match_peak_count)
        Sets the number of top abundant peaks to with theoretical ones
        """
        ...
    
    def getMatchPeakAllowedError(self) -> int:
        """
        Cython signature: size_t getMatchPeakAllowedError()
        Returns the number of top abundant peaks that are allowed not to match with a theoretical peak
        """
        ...
    
    def setMatchPeakAllowedError(self, match_peak_allowed_error: int ) -> None:
        """
        Cython signature: void setMatchPeakAllowedError(size_t match_peak_allowed_error)
        Sets the number of top abundant peaks that are allowed not to match with a theoretical peak
        """
        ...
    
    def getShowFragmentIons(self) -> bool:
        """
        Cython signature: bool getShowFragmentIons()
        Returns whether fragment ions shall be displayed
        """
        ...
    
    def setShowFragmentIons(self, show_fragments: bool ) -> None:
        """
        Cython signature: void setShowFragmentIons(bool show_fragments)
        Sets whether fragment ions shall be displayed
        """
        ...
    
    def getPrintDuplicateReferences(self) -> bool:
        """
        Cython signature: bool getPrintDuplicateReferences()
        Returns whether all proteins containing a found peptide should be displayed
        """
        ...
    
    def setPrintDuplicateReferences(self, print_duplicate_references: bool ) -> None:
        """
        Cython signature: void setPrintDuplicateReferences(bool print_duplicate_references)
        Sets whether all proteins containing a found peptide should be displayed
        """
        ...
    
    def getRemovePrecursorNearPeaks(self) -> bool:
        """
        Cython signature: bool getRemovePrecursorNearPeaks()
        Returns whether peaks near (15 amu) the precursor peak are removed
        """
        ...
    
    def setRemovePrecursorNearPeaks(self, remove_precursor_near_peaks: bool ) -> None:
        """
        Cython signature: void setRemovePrecursorNearPeaks(bool remove_precursor_near_peaks)
        Sets whether peaks near (15 amu) the precursor peak are removed
        """
        ...
    
    def getMassTypeParent(self) -> bool:
        """
        Cython signature: bool getMassTypeParent()
        Returns the mass type of the parent (0 - monoisotopic, 1 - average mass)
        """
        ...
    
    def setMassTypeParent(self, mass_type_parent: bool ) -> None:
        """
        Cython signature: void setMassTypeParent(bool mass_type_parent)
        Sets the mass type of the parent (0 - monoisotopic, 1 - average mass)
        """
        ...
    
    def getMassTypeFragment(self) -> bool:
        """
        Cython signature: bool getMassTypeFragment()
        Returns the mass type of the fragments (0 - monoisotopic, 1 - average mass)
        """
        ...
    
    def setMassTypeFragment(self, mass_type_fragment: bool ) -> None:
        """
        Cython signature: void setMassTypeFragment(bool mass_type_fragment)
        Sets the mass type of the fragments (0 - monoisotopic, 1 - average mass)
        """
        ...
    
    def getNormalizeXcorr(self) -> bool:
        """
        Cython signature: bool getNormalizeXcorr()
        Returns whether normalized xcorr values are displayed
        """
        ...
    
    def setNormalizeXcorr(self, normalize_xcorr: bool ) -> None:
        """
        Cython signature: void setNormalizeXcorr(bool normalize_xcorr)
        Sets whether normalized xcorr values are displayed
        """
        ...
    
    def getResiduesInUpperCase(self) -> bool:
        """
        Cython signature: bool getResiduesInUpperCase()
        Returns whether residues are in upper case
        """
        ...
    
    def setResiduesInUpperCase(self, residues_in_upper_case: bool ) -> None:
        """
        Cython signature: void setResiduesInUpperCase(bool residues_in_upper_case)
        Sets whether residues are in upper case
        """
        ...
    
    def addEnzymeInfo(self, enzyme_info: List[bytes] ) -> None:
        """
        Cython signature: void addEnzymeInfo(libcpp_vector[String] & enzyme_info)
        Adds an enzyme to the list and sets is as used
        """
        ...
    
    def handlePTMs(self, modification_line: Union[bytes, str, String] , modifications_filename: Union[bytes, str, String] , monoisotopic: bool ) -> None:
        """
        Cython signature: void handlePTMs(const String & modification_line, const String & modifications_filename, bool monoisotopic)
        """
        ...
    
    def __richcmp__(self, other: SequestInfile, op: int) -> Any:
        ... 


class StringView:
    """
    Cython implementation of _StringView

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1StringView.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void StringView()
        """
        ...
    
    @overload
    def __init__(self, in_0: bytes ) -> None:
        """
        Cython signature: void StringView(const libcpp_string &)
        """
        ...
    
    @overload
    def __init__(self, in_0: StringView ) -> None:
        """
        Cython signature: void StringView(StringView &)
        """
        ...
    
    def substr(self, start: int , end: int ) -> StringView:
        """
        Cython signature: StringView substr(size_t start, size_t end)
        """
        ...
    
    def size(self) -> int:
        """
        Cython signature: size_t size()
        """
        ...
    
    def getString(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getString()
        """
        ...
    
    def __richcmp__(self, other: StringView, op: int) -> Any:
        ... 


class TSE_Match:
    """
    Cython implementation of _TSE_Match

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1TSE_Match.html>`_
    """
    
    spectrum: MSSpectrum
    
    score: float
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void TSE_Match()
        """
        ...
    
    @overload
    def __init__(self, in_0: TSE_Match ) -> None:
        """
        Cython signature: void TSE_Match(TSE_Match &)
        """
        ...
    
    @overload
    def __init__(self, spectrum: MSSpectrum , score: float ) -> None:
        """
        Cython signature: void TSE_Match(MSSpectrum & spectrum, double score)
        """
        ... 


class TargetedSpectraExtractor:
    """
    Cython implementation of _TargetedSpectraExtractor

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1TargetedSpectraExtractor.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void TargetedSpectraExtractor()
        """
        ...
    
    @overload
    def __init__(self, in_0: TargetedSpectraExtractor ) -> None:
        """
        Cython signature: void TargetedSpectraExtractor(TargetedSpectraExtractor &)
        """
        ...
    
    def getDefaultParameters(self, in_0: Param ) -> None:
        """
        Cython signature: void getDefaultParameters(Param &)
        """
        ...
    
    @overload
    def annotateSpectra(self, in_0: List[MSSpectrum] , in_1: TargetedExperiment , in_2: List[MSSpectrum] , in_3: FeatureMap ) -> None:
        """
        Cython signature: void annotateSpectra(libcpp_vector[MSSpectrum] &, TargetedExperiment &, libcpp_vector[MSSpectrum] &, FeatureMap &)
        """
        ...
    
    @overload
    def annotateSpectra(self, in_0: List[MSSpectrum] , in_1: TargetedExperiment , in_2: List[MSSpectrum] ) -> None:
        """
        Cython signature: void annotateSpectra(libcpp_vector[MSSpectrum] &, TargetedExperiment &, libcpp_vector[MSSpectrum] &)
        """
        ...
    
    @overload
    def annotateSpectra(self, in_0: List[MSSpectrum] , in_1: FeatureMap , in_2: FeatureMap , in_3: List[MSSpectrum] ) -> None:
        """
        Cython signature: void annotateSpectra(libcpp_vector[MSSpectrum] &, FeatureMap &, FeatureMap &, libcpp_vector[MSSpectrum] &)
        """
        ...
    
    def searchSpectrum(self, in_0: FeatureMap , in_1: FeatureMap , in_2: bool ) -> None:
        """
        Cython signature: void searchSpectrum(FeatureMap &, FeatureMap &, bool)
        """
        ...
    
    def pickSpectrum(self, in_0: MSSpectrum , in_1: MSSpectrum ) -> None:
        """
        Cython signature: void pickSpectrum(MSSpectrum &, MSSpectrum &)
        """
        ...
    
    @overload
    def scoreSpectra(self, in_0: List[MSSpectrum] , in_1: List[MSSpectrum] , in_2: FeatureMap , in_3: List[MSSpectrum] ) -> None:
        """
        Cython signature: void scoreSpectra(libcpp_vector[MSSpectrum] &, libcpp_vector[MSSpectrum] &, FeatureMap &, libcpp_vector[MSSpectrum] &)
        """
        ...
    
    @overload
    def scoreSpectra(self, in_0: List[MSSpectrum] , in_1: List[MSSpectrum] , in_2: List[MSSpectrum] ) -> None:
        """
        Cython signature: void scoreSpectra(libcpp_vector[MSSpectrum] &, libcpp_vector[MSSpectrum] &, libcpp_vector[MSSpectrum] &)
        """
        ...
    
    @overload
    def selectSpectra(self, in_0: List[MSSpectrum] , in_1: FeatureMap , in_2: List[MSSpectrum] , in_3: FeatureMap ) -> None:
        """
        Cython signature: void selectSpectra(libcpp_vector[MSSpectrum] &, FeatureMap &, libcpp_vector[MSSpectrum] &, FeatureMap &)
        """
        ...
    
    @overload
    def selectSpectra(self, in_0: List[MSSpectrum] , in_1: List[MSSpectrum] ) -> None:
        """
        Cython signature: void selectSpectra(libcpp_vector[MSSpectrum] &, libcpp_vector[MSSpectrum] &)
        """
        ...
    
    @overload
    def extractSpectra(self, in_0: MSExperiment , in_1: TargetedExperiment , in_2: List[MSSpectrum] , in_3: FeatureMap , in_4: bool ) -> None:
        """
        Cython signature: void extractSpectra(MSExperiment &, TargetedExperiment &, libcpp_vector[MSSpectrum] &, FeatureMap &, bool)
        """
        ...
    
    @overload
    def extractSpectra(self, in_0: MSExperiment , in_1: TargetedExperiment , in_2: List[MSSpectrum] ) -> None:
        """
        Cython signature: void extractSpectra(MSExperiment &, TargetedExperiment &, libcpp_vector[MSSpectrum] &)
        """
        ...
    
    @overload
    def extractSpectra(self, in_0: MSExperiment , in_1: FeatureMap , in_2: List[MSSpectrum] ) -> None:
        """
        Cython signature: void extractSpectra(MSExperiment &, FeatureMap &, libcpp_vector[MSSpectrum] &)
        """
        ...
    
    def constructTransitionsList(self, in_0: FeatureMap , in_1: FeatureMap , in_2: TargetedExperiment ) -> None:
        """
        Cython signature: void constructTransitionsList(FeatureMap &, FeatureMap &, TargetedExperiment &)
        """
        ...
    
    def storeSpectraMSP(self, in_0: Union[bytes, str, String] , in_1: MSExperiment ) -> None:
        """
        Cython signature: void storeSpectraMSP(const String &, MSExperiment &)
        """
        ...
    
    def mergeFeatures(self, in_0: FeatureMap , in_1: FeatureMap ) -> None:
        """
        Cython signature: void mergeFeatures(FeatureMap &, FeatureMap &)
        """
        ...
    
    def getSubsections(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getSubsections()
        """
        ...
    
    def setParameters(self, param: Param ) -> None:
        """
        Cython signature: void setParameters(Param & param)
        Sets the parameters
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        Returns the parameters
        """
        ...
    
    def getDefaults(self) -> Param:
        """
        Cython signature: Param getDefaults()
        Returns the default parameters
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name
        """
        ...
    
    def setName(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String &)
        Sets the name
        """
        ... 


class TheoreticalIsotopePattern:
    """
    Cython implementation of _TheoreticalIsotopePattern

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::FeatureFinderAlgorithmPickedHelperStructs_1_1TheoreticalIsotopePattern.html>`_
    """
    
    intensity: List[float]
    
    optional_begin: int
    
    optional_end: int
    
    max: float
    
    trimmed_left: int
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void TheoreticalIsotopePattern()
        """
        ...
    
    @overload
    def __init__(self, in_0: TheoreticalIsotopePattern ) -> None:
        """
        Cython signature: void TheoreticalIsotopePattern(TheoreticalIsotopePattern &)
        """
        ...
    
    def size(self) -> int:
        """
        Cython signature: size_t size()
        """
        ... 


class TheoreticalSpectrumGenerator:
    """
    Cython implementation of _TheoreticalSpectrumGenerator

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1TheoreticalSpectrumGenerator.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void TheoreticalSpectrumGenerator()
        """
        ...
    
    @overload
    def __init__(self, in_0: TheoreticalSpectrumGenerator ) -> None:
        """
        Cython signature: void TheoreticalSpectrumGenerator(TheoreticalSpectrumGenerator &)
        """
        ...
    
    def getSpectrum(self, spec: MSSpectrum , peptide: AASequence , min_charge: int , max_charge: int ) -> None:
        """
        Cython signature: void getSpectrum(MSSpectrum & spec, AASequence & peptide, int min_charge, int max_charge)
        Generates a spectrum for a peptide sequence, with the ion types that are set in the tool parameters. If precursor_charge is set to 0 max_charge + 1 will be used
        """
        ...
    
    def getSubsections(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getSubsections()
        """
        ...
    
    def setParameters(self, param: Param ) -> None:
        """
        Cython signature: void setParameters(Param & param)
        Sets the parameters
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        Returns the parameters
        """
        ...
    
    def getDefaults(self) -> Param:
        """
        Cython signature: Param getDefaults()
        Returns the default parameters
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name
        """
        ...
    
    def setName(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String &)
        Sets the name
        """
        ... 


class TheoreticalSpectrumGeneratorXLMS:
    """
    Cython implementation of _TheoreticalSpectrumGeneratorXLMS

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1TheoreticalSpectrumGeneratorXLMS.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void TheoreticalSpectrumGeneratorXLMS()
        """
        ...
    
    @overload
    def __init__(self, in_0: TheoreticalSpectrumGeneratorXLMS ) -> None:
        """
        Cython signature: void TheoreticalSpectrumGeneratorXLMS(TheoreticalSpectrumGeneratorXLMS &)
        """
        ...
    
    def getLinearIonSpectrum(self, spectrum: MSSpectrum , peptide: AASequence , link_pos: int , frag_alpha: bool , charge: int , link_pos_2: int ) -> None:
        """
        Cython signature: void getLinearIonSpectrum(MSSpectrum & spectrum, AASequence peptide, size_t link_pos, bool frag_alpha, int charge, size_t link_pos_2)
            Generates fragment ions not containing the cross-linker for one peptide
        
            B-ions are generated from the beginning of the peptide up to the first linked position,
            y-ions are generated from the second linked position up the end of the peptide.
            If link_pos_2 is 0, a mono-link or cross-link is assumed and the second position is the same as the first position.
            For a loop-link two different positions can be set and link_pos_2 must be larger than link_pos
            The generated ion types and other additional settings are determined by the tool parameters
        
            :param spectrum: The spectrum to which the new peaks are added. Does not have to be empty, the generated peaks will be pushed onto it
            :param peptide: The peptide to fragment
            :param link_pos: The position of the cross-linker on the given peptide
            :param frag_alpha: True, if the fragmented peptide is the Alpha peptide. Used for ion-name annotation
            :param charge: The maximal charge of the ions
            :param link_pos_2: A second position for the linker, in case it is a loop link
        """
        ...
    
    @overload
    def getXLinkIonSpectrum(self, spectrum: MSSpectrum , peptide: AASequence , link_pos: int , precursor_mass: float , frag_alpha: bool , mincharge: int , maxcharge: int , link_pos_2: int ) -> None:
        """
        Cython signature: void getXLinkIonSpectrum(MSSpectrum & spectrum, AASequence peptide, size_t link_pos, double precursor_mass, bool frag_alpha, int mincharge, int maxcharge, size_t link_pos_2)
            Generates fragment ions containing the cross-linker for one peptide
        
            B-ions are generated from the first linked position up to the end of the peptide,
            y-ions are generated from the beginning of the peptide up to the second linked position.
            If link_pos_2 is 0, a mono-link or cross-link is assumed and the second position is the same as the first position.
            For a loop-link two different positions can be set and link_pos_2 must be larger than link_pos.
            Since in the case of a cross-link a whole second peptide is attached to the other side of the cross-link,
            a precursor mass for the two peptides and the linker is needed.
            In the case of a loop link the precursor mass is the mass of the only peptide and the linker.
            Although this function is more general, currently it is mainly used for loop-links and mono-links,
            because residues in the second, unknown peptide cannot be considered for possible neutral losses.
            The generated ion types and other additional settings are determined by the tool parameters
        
            :param spectrum: The spectrum to which the new peaks are added. Does not have to be empty, the generated peaks will be pushed onto it
            :param peptide: The peptide to fragment
            :param link_pos: The position of the cross-linker on the given peptide
            :param precursor_mass: The mass of the whole cross-link candidate or the precursor mass of the experimental MS2 spectrum.
            :param frag_alpha: True, if the fragmented peptide is the Alpha peptide. Used for ion-name annotation.
            :param mincharge: The minimal charge of the ions
            :param maxcharge: The maximal charge of the ions, it should be the precursor charge and is used to generate precursor ion peaks
            :param link_pos_2: A second position for the linker, in case it is a loop link
        """
        ...
    
    @overload
    def getXLinkIonSpectrum(self, spectrum: MSSpectrum , crosslink: ProteinProteinCrossLink , frag_alpha: bool , mincharge: int , maxcharge: int ) -> None:
        """
        Cython signature: void getXLinkIonSpectrum(MSSpectrum & spectrum, ProteinProteinCrossLink crosslink, bool frag_alpha, int mincharge, int maxcharge)
            Generates fragment ions containing the cross-linker for a pair of peptides
        
            B-ions are generated from the first linked position up to the end of the peptide,
            y-ions are generated from the beginning of the peptide up to the second linked position.
            This function generates neutral loss ions by considering both linked peptides.
            Only one of the peptides, decided by @frag_alpha, is fragmented.
            This function is not suitable to generate fragments for mono-links or loop-links.
            This simplifies the function, but it has to be called twice to get all fragments of a peptide pair.
            The generated ion types and other additional settings are determined by the tool parameters
        
            :param spectrum: The spectrum to which the new peaks are added. Does not have to be empty, the generated peaks will be pushed onto it
            :param crosslink: ProteinProteinCrossLink to be fragmented
            :param link_pos: The position of the cross-linker on the given peptide
            :param precursor_mass: The mass of the whole cross-link candidate or the precursor mass of the experimental MS2 spectrum
            :param frag_alpha: True, if the fragmented peptide is the Alpha peptide
            :param mincharge: The minimal charge of the ions
            :param maxcharge: The maximal charge of the ions, it should be the precursor charge and is used to generate precursor ion peaks
        """
        ...
    
    def getSubsections(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getSubsections()
        """
        ...
    
    def setParameters(self, param: Param ) -> None:
        """
        Cython signature: void setParameters(Param & param)
        Sets the parameters
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        Returns the parameters
        """
        ...
    
    def getDefaults(self) -> Param:
        """
        Cython signature: Param getDefaults()
        Returns the default parameters
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name
        """
        ...
    
    def setName(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String &)
        Sets the name
        """
        ... 


class XQuestScores:
    """
    Cython implementation of _XQuestScores

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1XQuestScores.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void XQuestScores()
        """
        ...
    
    @overload
    def __init__(self, in_0: XQuestScores ) -> None:
        """
        Cython signature: void XQuestScores(XQuestScores &)
        """
        ...
    
    @overload
    def preScore(self, matched_alpha: int , ions_alpha: int , matched_beta: int , ions_beta: int ) -> float:
        """
        Cython signature: float preScore(size_t matched_alpha, size_t ions_alpha, size_t matched_beta, size_t ions_beta)
        Compute a simple and fast to compute pre-score for a cross-link spectrum match
        
        :param matched_alpha: Number of experimental peaks matched to theoretical linear ions from the alpha peptide
        :param ions_alpha: Number of theoretical ions from the alpha peptide
        :param matched_beta: Number of experimental peaks matched to theoretical linear ions from the beta peptide
        :param ions_beta: Number of theoretical ions from the beta peptide
        """
        ...
    
    @overload
    def preScore(self, matched_alpha: int , ions_alpha: int ) -> float:
        """
        Cython signature: float preScore(size_t matched_alpha, size_t ions_alpha)
        Compute a simple and fast to compute pre-score for a mono-link spectrum match
        
        :param matched_alpha: Number of experimental peaks matched to theoretical linear ions from the alpha peptide
        :param ions_alpha: Number of theoretical ions from the alpha peptide
        """
        ...
    
    def matchOddsScore(self, theoretical_spec: MSSpectrum , fragment_mass_tolerance: float , fragment_mass_tolerance_unit_ppm: bool , is_xlink_spectrum: bool , n_charges: int ) -> float:
        """
        Cython signature: double matchOddsScore(MSSpectrum & theoretical_spec, double fragment_mass_tolerance, bool fragment_mass_tolerance_unit_ppm, bool is_xlink_spectrum, size_t n_charges)
        Compute the match-odds score, a score based on the probability of getting the given number of matched peaks by chance
        
        :param theoretical_spec: Theoretical spectrum, sorted by position
        :param matched_size: Alignment between the theoretical and the experimental spectra
        :param fragment_mass_tolerance: Fragment mass tolerance of the alignment
        :param fragment_mass_tolerance_unit_ppm: Fragment mass tolerance unit of the alignment, true = ppm, false = Da
        :param is_xlink_spectrum: Type of cross-link, true = cross-link, false = mono-link
        :param n_charges: Number of considered charges in the theoretical spectrum
        """
        ...
    
    def logOccupancyProb(self, theoretical_spec: MSSpectrum , matched_size: int , fragment_mass_tolerance: float , fragment_mass_tolerance_unit_ppm: bool ) -> float:
        """
        Cython signature: double logOccupancyProb(MSSpectrum theoretical_spec, size_t matched_size, double fragment_mass_tolerance, bool fragment_mass_tolerance_unit_ppm)
        Compute the logOccupancyProb score, similar to the match_odds, a score based on the probability of getting the given number of matched peaks by chance
        
        :param theoretical_spec: Theoretical spectrum, sorted by position
        :param matched_size: Number of matched peaks between experimental and theoretical spectra
        :param fragment_mass_tolerance: The tolerance of the alignment
        :param fragment_mass_tolerance_unit: The tolerance unit of the alignment, true = ppm, false = Da
        """
        ...
    
    def weightedTICScoreXQuest(self, alpha_size: int , beta_size: int , intsum_alpha: float , intsum_beta: float , total_current: float , type_is_cross_link: bool ) -> float:
        """
        Cython signature: double weightedTICScoreXQuest(size_t alpha_size, size_t beta_size, double intsum_alpha, double intsum_beta, double total_current, bool type_is_cross_link)
        """
        ...
    
    def weightedTICScore(self, alpha_size: int , beta_size: int , intsum_alpha: float , intsum_beta: float , total_current: float , type_is_cross_link: bool ) -> float:
        """
        Cython signature: double weightedTICScore(size_t alpha_size, size_t beta_size, double intsum_alpha, double intsum_beta, double total_current, bool type_is_cross_link)
        """
        ...
    
    def matchedCurrentChain(self, matched_spec_common: List[List[int, int]] , matched_spec_xlinks: List[List[int, int]] , spectrum_common_peaks: MSSpectrum , spectrum_xlink_peaks: MSSpectrum ) -> float:
        """
        Cython signature: double matchedCurrentChain(libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_common, libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_xlinks, MSSpectrum & spectrum_common_peaks, MSSpectrum & spectrum_xlink_peaks)
        """
        ...
    
    def totalMatchedCurrent(self, matched_spec_common_alpha: List[List[int, int]] , matched_spec_common_beta: List[List[int, int]] , matched_spec_xlinks_alpha: List[List[int, int]] , matched_spec_xlinks_beta: List[List[int, int]] , spectrum_common_peaks: MSSpectrum , spectrum_xlink_peaks: MSSpectrum ) -> float:
        """
        Cython signature: double totalMatchedCurrent(libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_common_alpha, libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_common_beta, libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_xlinks_alpha, libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_xlinks_beta, MSSpectrum & spectrum_common_peaks, MSSpectrum & spectrum_xlink_peaks)
        """
        ...
    
    def xCorrelation(self, spec1: MSSpectrum , spec2: MSSpectrum , maxshift: int , tolerance: float ) -> List[float]:
        """
        Cython signature: libcpp_vector[double] xCorrelation(MSSpectrum & spec1, MSSpectrum & spec2, int maxshift, double tolerance)
        """
        ...
    
    def xCorrelationPrescore(self, spec1: MSSpectrum , spec2: MSSpectrum , tolerance: float ) -> float:
        """
        Cython signature: double xCorrelationPrescore(MSSpectrum & spec1, MSSpectrum & spec2, double tolerance)
        """
        ... 


class __ChromatogramType:
    None
    MASS_CHROMATOGRAM : int
    TOTAL_ION_CURRENT_CHROMATOGRAM : int
    SELECTED_ION_CURRENT_CHROMATOGRAM : int
    BASEPEAK_CHROMATOGRAM : int
    SELECTED_ION_MONITORING_CHROMATOGRAM : int
    SELECTED_REACTION_MONITORING_CHROMATOGRAM : int
    ELECTROMAGNETIC_RADIATION_CHROMATOGRAM : int
    ABSORPTION_CHROMATOGRAM : int
    EMISSION_CHROMATOGRAM : int
    SIZE_OF_CHROMATOGRAM_TYPE : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __DerivatizationAgent:
    None
    NOT_SELECTED : int
    TBDMS : int
    SIZE_OF_DERIVATIZATIONAGENT : int

    def getMapping(self) -> Dict[int, str]:
       ...
    DerivatizationAgent : __DerivatizationAgent 


class __FilterOperation:
    None
    GREATER_EQUAL : int
    EQUAL : int
    LESS_EQUAL : int
    EXISTS : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __FilterType:
    None
    INTENSITY : int
    QUALITY : int
    CHARGE : int
    SIZE : int
    META_DATA : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class ITRAQ_TYPES:
    None
    FOURPLEX : int
    EIGHTPLEX : int
    TMT_SIXPLEX : int
    SIZE_OF_ITRAQ_TYPES : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __MassIntensityType:
    None
    NORM_MAX : int
    NORM_SUM : int
    SIZE_OF_MASSINTENSITYTYPE : int

    def getMapping(self) -> Dict[int, str]:
       ...
    MassIntensityType : __MassIntensityType 


class TermSpecificityNuc:
    None
    ANYWHERE : int
    FIVE_PRIME : int
    THREE_PRIME : int
    NUMBER_OF_TERM_SPECIFICITY : int

    def getMapping(self) -> Dict[int, str]:
       ... 

