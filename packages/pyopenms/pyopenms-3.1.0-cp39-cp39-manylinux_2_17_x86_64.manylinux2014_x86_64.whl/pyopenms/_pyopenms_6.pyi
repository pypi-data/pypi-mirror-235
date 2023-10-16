from __future__ import annotations
from typing import overload, Any, List, Dict, Tuple, Set, Sequence, Union
from pyopenms import *  # pylint: disable=wildcard-import; lgtm(py/polluting-import)
import numpy as _np

from enum import Enum as _PyEnum


def __static_IonIdentityMolecularNetworking_annotateConsensusMap(consensus_map: ConsensusMap ) -> None:
    """
    Cython signature: void annotateConsensusMap(ConsensusMap & consensus_map)
        Annotate ConsensusMap for ion identity molecular networking (IIMN) workflow by GNPS.
        
        Adds meta values Constants::UserParams::IIMN_ROW_ID (unique index for each feature), Constants::UserParams::IIMN_ADDUCT_PARTNERS (related features row IDs)
        and Constants::UserParams::IIMN_ANNOTATION_NETWORK_NUMBER (all related features with different adduct states) get the same network number).
        This method requires the features annotated with the Constants::UserParams::IIMN_LINKED_GROUPS meta value.
        If at least one of the features has an annotation for Constants::UserParam::IIMN_LINKED_GROUPS, annotate ConsensusMap for IIMN.
        
        
        :param consensus_map: Input ConsensusMap without IIMN annotations.
    """
    ...

def __static_TransformationModelBSpline_getDefaultParameters(params: Param ) -> None:
    """
    Cython signature: void getDefaultParameters(Param & params)
    """
    ...

def __static_FeatureFinderAlgorithmPicked_getProductName() -> Union[bytes, str, String]:
    """
    Cython signature: String getProductName()
    """
    ...

def __static_CsiFingerIdMzTabWriter_read(sirius_output_paths: List[bytes] , original_input_mzml: Union[bytes, str, String] , top_n_hits: int , result: MzTab ) -> None:
    """
    Cython signature: void read(libcpp_vector[String] & sirius_output_paths, const String & original_input_mzml, size_t top_n_hits, MzTab & result)
    """
    ...

def __static_IonIdentityMolecularNetworking_writeSupplementaryPairTable(consensus_map: ConsensusMap , output_file: Union[bytes, str, String] ) -> None:
    """
    Cython signature: void writeSupplementaryPairTable(const ConsensusMap & consensus_map, const String & output_file)
        Write supplementary pair table (csv file) from a ConsensusMap with edge annotations for connected features. Required for GNPS IIMN.
        
        The table contains the columns "ID 1" (row ID of first feature), "ID 2" (row ID of second feature), "EdgeType" (MS1/2 annotation),
        "Score" (the number of direct partners from both connected features) and "Annotation" (adducts and delta m/z between two connected features).
        
        
        :param consensus_map: Input ConsensusMap annotated with IonIdentityMolecularNetworking.annotateConsensusMap.
        :param output_file: Output file path for the supplementary pair table.
    """
    ...


class AQS_featureConcentration:
    """
    Cython implementation of _AQS_featureConcentration

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1AQS_featureConcentration.html>`_
    """
    
    feature: Feature
    
    IS_feature: Feature
    
    actual_concentration: float
    
    IS_actual_concentration: float
    
    concentration_units: Union[bytes, str, String]
    
    dilution_factor: float
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void AQS_featureConcentration()
        """
        ...
    
    @overload
    def __init__(self, in_0: AQS_featureConcentration ) -> None:
        """
        Cython signature: void AQS_featureConcentration(AQS_featureConcentration &)
        """
        ... 


class AQS_runConcentration:
    """
    Cython implementation of _AQS_runConcentration

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1AQS_runConcentration.html>`_
    """
    
    sample_name: Union[bytes, str, String]
    
    component_name: Union[bytes, str, String]
    
    IS_component_name: Union[bytes, str, String]
    
    actual_concentration: float
    
    IS_actual_concentration: float
    
    concentration_units: Union[bytes, str, String]
    
    dilution_factor: float
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void AQS_runConcentration()
        """
        ...
    
    @overload
    def __init__(self, in_0: AQS_runConcentration ) -> None:
        """
        Cython signature: void AQS_runConcentration(AQS_runConcentration &)
        """
        ... 


class AScore:
    """
    Cython implementation of _AScore

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1AScore.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void AScore()
        """
        ...
    
    @overload
    def __init__(self, in_0: AScore ) -> None:
        """
        Cython signature: void AScore(AScore &)
        """
        ...
    
    def compute(self, hit: PeptideHit , real_spectrum: MSSpectrum ) -> PeptideHit:
        """
        Cython signature: PeptideHit compute(PeptideHit & hit, MSSpectrum & real_spectrum)
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


class AbsoluteQuantitationStandards:
    """
    Cython implementation of _AbsoluteQuantitationStandards

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1AbsoluteQuantitationStandards.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void AbsoluteQuantitationStandards()
        """
        ...
    
    @overload
    def __init__(self, in_0: AbsoluteQuantitationStandards ) -> None:
        """
        Cython signature: void AbsoluteQuantitationStandards(AbsoluteQuantitationStandards &)
        """
        ...
    
    def getComponentFeatureConcentrations(self, run_concentrations: List[AQS_runConcentration] , feature_maps: List[FeatureMap] , component_name: Union[bytes, str, String] , feature_concentrations: List[AQS_featureConcentration] ) -> None:
        """
        Cython signature: void getComponentFeatureConcentrations(libcpp_vector[AQS_runConcentration] & run_concentrations, libcpp_vector[FeatureMap] & feature_maps, const String & component_name, libcpp_vector[AQS_featureConcentration] & feature_concentrations)
        """
        ... 


class AccurateMassSearchEngine:
    """
    Cython implementation of _AccurateMassSearchEngine

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1AccurateMassSearchEngine.html>`_
      -- Inherits from ['DefaultParamHandler', 'ProgressLogger']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void AccurateMassSearchEngine()
        """
        ...
    
    @overload
    def __init__(self, in_0: AccurateMassSearchEngine ) -> None:
        """
        Cython signature: void AccurateMassSearchEngine(AccurateMassSearchEngine &)
        """
        ...
    
    def queryByMZ(self, observed_mz: float , observed_charge: int , ion_mode: Union[bytes, str, String] , in_3: List[AccurateMassSearchResult] , observed_adduct: EmpiricalFormula ) -> None:
        """
        Cython signature: void queryByMZ(double observed_mz, int observed_charge, String ion_mode, libcpp_vector[AccurateMassSearchResult] &, EmpiricalFormula & observed_adduct)
        """
        ...
    
    def queryByFeature(self, feature: Feature , feature_index: int , ion_mode: Union[bytes, str, String] , in_3: List[AccurateMassSearchResult] ) -> None:
        """
        Cython signature: void queryByFeature(Feature feature, size_t feature_index, String ion_mode, libcpp_vector[AccurateMassSearchResult] &)
        """
        ...
    
    def queryByConsensusFeature(self, cfeat: ConsensusFeature , cf_index: int , number_of_maps: int , ion_mode: Union[bytes, str, String] , results: List[AccurateMassSearchResult] ) -> None:
        """
        Cython signature: void queryByConsensusFeature(ConsensusFeature cfeat, size_t cf_index, size_t number_of_maps, String ion_mode, libcpp_vector[AccurateMassSearchResult] & results)
        """
        ...
    
    @overload
    def run(self, in_0: FeatureMap , in_1: MzTab ) -> None:
        """
        Cython signature: void run(FeatureMap &, MzTab &)
        """
        ...
    
    @overload
    def run(self, in_0: FeatureMap , in_1: MzTabM ) -> None:
        """
        Cython signature: void run(FeatureMap &, MzTabM &)
        """
        ...
    
    @overload
    def run(self, in_0: ConsensusMap , in_1: MzTab ) -> None:
        """
        Cython signature: void run(ConsensusMap &, MzTab &)
        """
        ...
    
    def init(self) -> None:
        """
        Cython signature: void init()
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


class AnalysisSummary:
    """
    Cython implementation of _AnalysisSummary

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1AnalysisSummary.html>`_
    """
    
    user_params_: MetaInfo
    
    cv_params_: CVTermList
    
    quant_type_: int
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void AnalysisSummary()
        """
        ...
    
    @overload
    def __init__(self, in_0: AnalysisSummary ) -> None:
        """
        Cython signature: void AnalysisSummary(AnalysisSummary &)
        """
        ... 


class Assay:
    """
    Cython implementation of _Assay

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1Assay.html>`_
    """
    
    uid_: Union[bytes, str, String]
    
    raw_files_: List[ExperimentalSettings]
    
    feature_maps_: Dict[int, FeatureMap]
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void Assay()
        """
        ...
    
    @overload
    def __init__(self, in_0: Assay ) -> None:
        """
        Cython signature: void Assay(Assay &)
        """
        ... 


class BiGaussFitter1D:
    """
    Cython implementation of _BiGaussFitter1D

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1BiGaussFitter1D.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void BiGaussFitter1D()
        """
        ...
    
    @overload
    def __init__(self, in_0: BiGaussFitter1D ) -> None:
        """
        Cython signature: void BiGaussFitter1D(BiGaussFitter1D &)
        """
        ...
    
    def getProductName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getProductName()
        Name of the model (needed by Factory)
        """
        ... 


class ChargedIndexSet:
    """
    Cython implementation of _ChargedIndexSet

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ChargedIndexSet.html>`_
    """
    
    charge: int
    
    def __init__(self) -> None:
        """
        Cython signature: void ChargedIndexSet()
        Index set with associated charge estimate
        """
        ... 


class ConfidenceScoring:
    """
    Cython implementation of _ConfidenceScoring

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ConfidenceScoring.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ConfidenceScoring()
        """
        ...
    
    @overload
    def __init__(self, in_0: ConfidenceScoring ) -> None:
        """
        Cython signature: void ConfidenceScoring(ConfidenceScoring &)
        """
        ...
    
    def initialize(self, targeted: TargetedExperiment , n_decoys: int , n_transitions: int , trafo: TransformationDescription ) -> None:
        """
        Cython signature: void initialize(TargetedExperiment & targeted, size_t n_decoys, size_t n_transitions, TransformationDescription trafo)
        """
        ...
    
    def initializeGlm(self, intercept: float , rt_coef: float , int_coef: float ) -> None:
        """
        Cython signature: void initializeGlm(double intercept, double rt_coef, double int_coef)
        """
        ...
    
    def scoreMap(self, map: FeatureMap ) -> None:
        """
        Cython signature: void scoreMap(FeatureMap & map)
        Score a feature map -> make sure the class is properly initialized
        """
        ... 


class ConsensusIDAlgorithmPEPIons:
    """
    Cython implementation of _ConsensusIDAlgorithmPEPIons

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ConsensusIDAlgorithmPEPIons.html>`_
      -- Inherits from ['ConsensusIDAlgorithmSimilarity']
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void ConsensusIDAlgorithmPEPIons()
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


class ConsensusIDAlgorithmRanks:
    """
    Cython implementation of _ConsensusIDAlgorithmRanks

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ConsensusIDAlgorithmRanks.html>`_
      -- Inherits from ['ConsensusIDAlgorithmIdentity']
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void ConsensusIDAlgorithmRanks()
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


class CsiFingerIdMzTabWriter:
    """
    Cython implementation of _CsiFingerIdMzTabWriter

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1CsiFingerIdMzTabWriter.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void CsiFingerIdMzTabWriter()
        """
        ...
    
    @overload
    def __init__(self, in_0: CsiFingerIdMzTabWriter ) -> None:
        """
        Cython signature: void CsiFingerIdMzTabWriter(CsiFingerIdMzTabWriter &)
        """
        ...
    
    read: __static_CsiFingerIdMzTabWriter_read 


class DigestionEnzyme:
    """
    Cython implementation of _DigestionEnzyme

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1DigestionEnzyme.html>`_

      Base class for digestion enzymes
    """
    
    @overload
    def __init__(self, in_0: DigestionEnzyme ) -> None:
        """
        Cython signature: void DigestionEnzyme(DigestionEnzyme &)
        """
        ...
    
    @overload
    def __init__(self, name: Union[bytes, str, String] , cleavage_regex: Union[bytes, str, String] , synonyms: Set[bytes] , regex_description: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void DigestionEnzyme(const String & name, const String & cleavage_regex, libcpp_set[String] & synonyms, String regex_description)
        """
        ...
    
    def setName(self, name: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String & name)
        Sets the name of the enzyme
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        Returns the name of the enzyme
        """
        ...
    
    def setSynonyms(self, synonyms: Set[bytes] ) -> None:
        """
        Cython signature: void setSynonyms(libcpp_set[String] & synonyms)
        Sets the synonyms
        """
        ...
    
    def addSynonym(self, synonym: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void addSynonym(const String & synonym)
        Adds a synonym
        """
        ...
    
    def getSynonyms(self) -> Set[bytes]:
        """
        Cython signature: libcpp_set[String] getSynonyms()
        Returns the synonyms
        """
        ...
    
    def setRegEx(self, cleavage_regex: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setRegEx(const String & cleavage_regex)
        Sets the cleavage regex
        """
        ...
    
    def getRegEx(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getRegEx()
        Returns the cleavage regex
        """
        ...
    
    def setRegExDescription(self, value: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setRegExDescription(const String & value)
        Sets the regex description
        """
        ...
    
    def getRegExDescription(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getRegExDescription()
        Returns the regex description
        """
        ...
    
    def setValueFromFile(self, key: Union[bytes, str, String] , value: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool setValueFromFile(String key, String value)
        Sets the value of a member variable based on an entry from an input file
        """
        ...
    
    def __richcmp__(self, other: DigestionEnzyme, op: int) -> Any:
        ... 


class FeatureFinder:
    """
    Cython implementation of _FeatureFinder

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureFinder.html>`_
      -- Inherits from ['ProgressLogger']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void FeatureFinder()
        """
        ...
    
    @overload
    def __init__(self, in_0: FeatureFinder ) -> None:
        """
        Cython signature: void FeatureFinder(FeatureFinder &)
        """
        ...
    
    def run(self, algorithm_name: Union[bytes, str, String] , input_map: MSExperiment , feats: FeatureMap , param: Param , seeds: FeatureMap ) -> None:
        """
        Cython signature: void run(String algorithm_name, MSExperiment & input_map, FeatureMap & feats, Param & param, FeatureMap & seeds)
        Executes the FeatureFinder using the given algorithm\n
        There are several constraints for the `input_map`.  They are tested before the algorithm starts.  It must only contain MS 1 level scans and you have to call updateRanges() before passing it to this method
        The input map is sorted by RT & m/z if that's not the case
        Furthermore we throw an Exception if the data contains negative m/z values,
        as this will disturb most algorithms
        
        
        :param algorithm_name: Name of the feature finding algorithm to use
        :param input_map: Input peak map
        :param features: Output feature map
        :param param: Algorithm parameters
        :param seeds: List of seeds to use
        """
        ...
    
    def getParameters(self, algorithm_name: Union[bytes, str, String] ) -> Param:
        """
        Cython signature: Param getParameters(String algorithm_name)
        Returns the default parameters for the algorithm with name `algorithm_name`
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


class FeatureFinderAlgorithmPicked:
    """
    Cython implementation of _FeatureFinderAlgorithmPicked

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureFinderAlgorithmPicked.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void FeatureFinderAlgorithmPicked()
        """
        ...
    
    def setData(self, input: MSExperiment , output: FeatureMap , ff: FeatureFinder ) -> None:
        """
        Cython signature: void setData(MSExperiment & input, FeatureMap & output, FeatureFinder & ff)
        """
        ...
    
    def run(self) -> None:
        """
        Cython signature: void run()
        """
        ...
    
    def setSeeds(self, seeds: FeatureMap ) -> None:
        """
        Cython signature: void setSeeds(FeatureMap & seeds)
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
    
    getProductName: __static_FeatureFinderAlgorithmPicked_getProductName 


class FeatureFinderIdentificationAlgorithm:
    """
    Cython implementation of _FeatureFinderIdentificationAlgorithm

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureFinderIdentificationAlgorithm.html>`_
      -- Inherits from ['DefaultParamHandler']

    Algorithm class for FeatureFinderIdentification
    
    External IDs (peptides_ext, proteins_ext) may be empty,
    in which case no machine learning or FDR estimation will be performed.
    Optional seeds from e.g. untargeted FeatureFinders can be added with
    seeds.
    Results will be written to features .
    Caution: peptide IDs will be shrunk to best hit, FFid metavalues added
    and potential seed IDs added.
    
    Usage:
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void FeatureFinderIdentificationAlgorithm()
        """
        ...
    
    @overload
    def run(self, peptides: List[PeptideIdentification] , proteins: List[ProteinIdentification] , peptides_ext: List[PeptideIdentification] , proteins_ext: List[ProteinIdentification] , features: FeatureMap ) -> None:
        """
        Cython signature: void run(libcpp_vector[PeptideIdentification] peptides, libcpp_vector[ProteinIdentification] & proteins, libcpp_vector[PeptideIdentification] peptides_ext, libcpp_vector[ProteinIdentification] proteins_ext, FeatureMap & features)
        Run feature detection
        
        
        :param peptides: Vector of identified peptides
        :param proteins: Vector of identified proteins
        :param peptides_ext: Vector of external identified peptides, can be used to transfer ids from other runs
        :param proteins_ext: Vector of external identified proteins, can be used to transfer ids from other runs
        :param features: Feature detection results will be added here
        """
        ...
    
    @overload
    def run(self, peptides: List[PeptideIdentification] , proteins: List[ProteinIdentification] , peptides_ext: List[PeptideIdentification] , proteins_ext: List[ProteinIdentification] , features: FeatureMap , seeds: FeatureMap ) -> None:
        """
        Cython signature: void run(libcpp_vector[PeptideIdentification] peptides, libcpp_vector[ProteinIdentification] & proteins, libcpp_vector[PeptideIdentification] peptides_ext, libcpp_vector[ProteinIdentification] proteins_ext, FeatureMap & features, FeatureMap & seeds)
        Run feature detection
        
        
        :param peptides: Vector of identified peptides
        :param proteins: Vector of identified proteins
        :param peptides_ext: Vector of external identified peptides, can be used to transfer ids from other runs
        :param proteins_ext: Vector of external identified proteins, can be used to transfer ids from other runs
        :param features: Feature detection results will be added here
        :param seeds: Optional seeds for feature detection from e.g. untargeted FeatureFinders
        """
        ...
    
    @overload
    def run(self, peptides: List[PeptideIdentification] , proteins: List[ProteinIdentification] , peptides_ext: List[PeptideIdentification] , proteins_ext: List[ProteinIdentification] , features: FeatureMap , seeds: FeatureMap , spectra_file: String ) -> None:
        """
        Cython signature: void run(libcpp_vector[PeptideIdentification] peptides, libcpp_vector[ProteinIdentification] & proteins, libcpp_vector[PeptideIdentification] peptides_ext, libcpp_vector[ProteinIdentification] proteins_ext, FeatureMap & features, FeatureMap & seeds, String & spectra_file)
        Run feature detection
        
        
        :param peptides: Vector of identified peptides
        :param proteins: Vector of identified proteins
        :param peptides_ext: Vector of external identified peptides, can be used to transfer ids from other runs
        :param proteins_ext: Vector of external identified proteins, can be used to transfer ids from other runs
        :param features: Feature detection results will be added here
        :param seeds: Optional seeds for feature detection from e.g. untargeted FeatureFinders
        :param spectra_file: Path will be stored in features in case the MSExperiment has no proper primaryMSRunPath
        """
        ...
    
    def runOnCandidates(self, features: FeatureMap ) -> None:
        """
        Cython signature: void runOnCandidates(FeatureMap & features)
        Run feature detection on identified features (e.g. loaded from an IdXML file)
        """
        ...
    
    def setMSData(self, in_0: MSExperiment ) -> None:
        """
        Cython signature: void setMSData(const MSExperiment &)
        Sets ms data
        """
        ...
    
    def getMSData(self) -> MSExperiment:
        """
        Cython signature: MSExperiment getMSData()
        Returns ms data as MSExperiment
        """
        ...
    
    def getChromatograms(self) -> MSExperiment:
        """
        Cython signature: MSExperiment getChromatograms()
        Returns chromatogram data as MSExperiment
        """
        ...
    
    def getLibrary(self) -> TargetedExperiment:
        """
        Cython signature: TargetedExperiment getLibrary()
        Returns constructed assay library
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


class GNPSMGFFile:
    """
    Cython implementation of _GNPSMGFFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1GNPSMGFFile.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void GNPSMGFFile()
        """
        ...
    
    @overload
    def __init__(self, in_0: GNPSMGFFile ) -> None:
        """
        Cython signature: void GNPSMGFFile(GNPSMGFFile &)
        """
        ...
    
    def store(self, consensus_file_path: Union[bytes, str, String] , mzml_file_paths: List[bytes] , out: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void store(const String & consensus_file_path, const StringList & mzml_file_paths, const String & out)
        Export consensus file from default workflow to GNPS MGF format
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


class GaussFilter:
    """
    Cython implementation of _GaussFilter

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1GaussFilter.html>`_
      -- Inherits from ['DefaultParamHandler', 'ProgressLogger']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void GaussFilter()
        This class represents a Gaussian lowpass-filter which works on uniform as well as on non-uniform profile data
        """
        ...
    
    @overload
    def __init__(self, in_0: GaussFilter ) -> None:
        """
        Cython signature: void GaussFilter(GaussFilter &)
        """
        ...
    
    @overload
    def filter(self, spectrum: MSSpectrum ) -> None:
        """
        Cython signature: void filter(MSSpectrum & spectrum)
        Smoothes an MSSpectrum containing profile data
        """
        ...
    
    @overload
    def filter(self, chromatogram: MSChromatogram ) -> None:
        """
        Cython signature: void filter(MSChromatogram & chromatogram)
        """
        ...
    
    def filterExperiment(self, exp: MSExperiment ) -> None:
        """
        Cython signature: void filterExperiment(MSExperiment & exp)
        Smoothes an MSExperiment containing profile data
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


class IMSElement:
    """
    Cython implementation of _IMSElement

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::ims::IMSElement_1_1IMSElement.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void IMSElement()
        Represents a chemical atom with name and isotope distribution
        """
        ...
    
    @overload
    def __init__(self, in_0: IMSElement ) -> None:
        """
        Cython signature: void IMSElement(IMSElement &)
        """
        ...
    
    @overload
    def __init__(self, name: bytes , isotopes: IMSIsotopeDistribution ) -> None:
        """
        Cython signature: void IMSElement(libcpp_string & name, IMSIsotopeDistribution & isotopes)
        """
        ...
    
    @overload
    def __init__(self, name: bytes , mass: float ) -> None:
        """
        Cython signature: void IMSElement(libcpp_string & name, double mass)
        """
        ...
    
    @overload
    def __init__(self, name: bytes , nominal_mass: int ) -> None:
        """
        Cython signature: void IMSElement(libcpp_string & name, unsigned int nominal_mass)
        """
        ...
    
    def getName(self) -> bytes:
        """
        Cython signature: libcpp_string getName()
        Gets element's name
        """
        ...
    
    def setName(self, name: bytes ) -> None:
        """
        Cython signature: void setName(libcpp_string & name)
        Sets element's name
        """
        ...
    
    def getSequence(self) -> bytes:
        """
        Cython signature: libcpp_string getSequence()
        Gets element's sequence
        """
        ...
    
    def setSequence(self, sequence: bytes ) -> None:
        """
        Cython signature: void setSequence(libcpp_string & sequence)
        Sets element's sequence
        """
        ...
    
    def getNominalMass(self) -> int:
        """
        Cython signature: unsigned int getNominalMass()
        Gets element's nominal mass
        """
        ...
    
    def getMass(self, index: int ) -> float:
        """
        Cython signature: double getMass(int index)
        Gets mass of element's isotope 'index'
        """
        ...
    
    def getAverageMass(self) -> float:
        """
        Cython signature: double getAverageMass()
        Gets element's average mass
        """
        ...
    
    def getIonMass(self, electrons_number: int ) -> float:
        """
        Cython signature: double getIonMass(int electrons_number)
        Gets ion mass of element. By default ion lacks 1 electron, but this can be changed by setting other 'electrons_number'
        """
        ...
    
    def getIsotopeDistribution(self) -> IMSIsotopeDistribution:
        """
        Cython signature: IMSIsotopeDistribution getIsotopeDistribution()
        Gets element's isotope distribution
        """
        ...
    
    def setIsotopeDistribution(self, isotopes: IMSIsotopeDistribution ) -> None:
        """
        Cython signature: void setIsotopeDistribution(IMSIsotopeDistribution & isotopes)
        Sets element's isotope distribution
        """
        ...
    
    def __richcmp__(self, other: IMSElement, op: int) -> Any:
        ... 


class IncludeExcludeTarget:
    """
    Cython implementation of _IncludeExcludeTarget

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1IncludeExcludeTarget.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void IncludeExcludeTarget()
        This class stores a SRM/MRM transition
        """
        ...
    
    @overload
    def __init__(self, in_0: IncludeExcludeTarget ) -> None:
        """
        Cython signature: void IncludeExcludeTarget(IncludeExcludeTarget &)
        """
        ...
    
    def setName(self, name: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setName(const String & name)
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        """
        ...
    
    def setPeptideRef(self, peptide_ref: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setPeptideRef(const String & peptide_ref)
        """
        ...
    
    def getPeptideRef(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getPeptideRef()
        """
        ...
    
    def setCompoundRef(self, compound_ref: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setCompoundRef(const String & compound_ref)
        """
        ...
    
    def getCompoundRef(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getCompoundRef()
        """
        ...
    
    def setPrecursorMZ(self, mz: float ) -> None:
        """
        Cython signature: void setPrecursorMZ(double mz)
        """
        ...
    
    def getPrecursorMZ(self) -> float:
        """
        Cython signature: double getPrecursorMZ()
        """
        ...
    
    def setPrecursorCVTermList(self, list_: CVTermList ) -> None:
        """
        Cython signature: void setPrecursorCVTermList(CVTermList & list_)
        """
        ...
    
    def addPrecursorCVTerm(self, cv_term: CVTerm ) -> None:
        """
        Cython signature: void addPrecursorCVTerm(CVTerm & cv_term)
        """
        ...
    
    def getPrecursorCVTermList(self) -> CVTermList:
        """
        Cython signature: CVTermList getPrecursorCVTermList()
        """
        ...
    
    def setProductMZ(self, mz: float ) -> None:
        """
        Cython signature: void setProductMZ(double mz)
        """
        ...
    
    def getProductMZ(self) -> float:
        """
        Cython signature: double getProductMZ()
        """
        ...
    
    def setProductCVTermList(self, list_: CVTermList ) -> None:
        """
        Cython signature: void setProductCVTermList(CVTermList & list_)
        """
        ...
    
    def addProductCVTerm(self, cv_term: CVTerm ) -> None:
        """
        Cython signature: void addProductCVTerm(CVTerm & cv_term)
        """
        ...
    
    def getProductCVTermList(self) -> CVTermList:
        """
        Cython signature: CVTermList getProductCVTermList()
        """
        ...
    
    def setInterpretations(self, interpretations: List[CVTermList] ) -> None:
        """
        Cython signature: void setInterpretations(libcpp_vector[CVTermList] & interpretations)
        """
        ...
    
    def getInterpretations(self) -> List[CVTermList]:
        """
        Cython signature: libcpp_vector[CVTermList] getInterpretations()
        """
        ...
    
    def addInterpretation(self, interpretation: CVTermList ) -> None:
        """
        Cython signature: void addInterpretation(CVTermList & interpretation)
        """
        ...
    
    def setConfigurations(self, configuration: List[Configuration] ) -> None:
        """
        Cython signature: void setConfigurations(libcpp_vector[Configuration] & configuration)
        """
        ...
    
    def getConfigurations(self) -> List[Configuration]:
        """
        Cython signature: libcpp_vector[Configuration] getConfigurations()
        """
        ...
    
    def addConfiguration(self, configuration: Configuration ) -> None:
        """
        Cython signature: void addConfiguration(Configuration & configuration)
        """
        ...
    
    def setPrediction(self, prediction: CVTermList ) -> None:
        """
        Cython signature: void setPrediction(CVTermList & prediction)
        """
        ...
    
    def addPredictionTerm(self, prediction: CVTerm ) -> None:
        """
        Cython signature: void addPredictionTerm(CVTerm & prediction)
        """
        ...
    
    def getPrediction(self) -> CVTermList:
        """
        Cython signature: CVTermList getPrediction()
        """
        ...
    
    def setRetentionTime(self, rt: RetentionTime ) -> None:
        """
        Cython signature: void setRetentionTime(RetentionTime rt)
        """
        ...
    
    def getRetentionTime(self) -> RetentionTime:
        """
        Cython signature: RetentionTime getRetentionTime()
        """
        ...
    
    def setCVTerms(self, terms: List[CVTerm] ) -> None:
        """
        Cython signature: void setCVTerms(libcpp_vector[CVTerm] & terms)
        """
        ...
    
    def replaceCVTerm(self, term: CVTerm ) -> None:
        """
        Cython signature: void replaceCVTerm(CVTerm & term)
        """
        ...
    
    @overload
    def replaceCVTerms(self, cv_terms: List[CVTerm] , accession: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void replaceCVTerms(libcpp_vector[CVTerm] cv_terms, String accession)
        """
        ...
    
    @overload
    def replaceCVTerms(self, cv_term_map: Dict[bytes,List[CVTerm]] ) -> None:
        """
        Cython signature: void replaceCVTerms(libcpp_map[String,libcpp_vector[CVTerm]] cv_term_map)
        """
        ...
    
    def getCVTerms(self) -> Dict[bytes,List[CVTerm]]:
        """
        Cython signature: libcpp_map[String,libcpp_vector[CVTerm]] getCVTerms()
        """
        ...
    
    def addCVTerm(self, term: CVTerm ) -> None:
        """
        Cython signature: void addCVTerm(CVTerm & term)
        """
        ...
    
    def hasCVTerm(self, accession: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool hasCVTerm(String accession)
        """
        ...
    
    def empty(self) -> bool:
        """
        Cython signature: bool empty()
        """
        ...
    
    def __richcmp__(self, other: IncludeExcludeTarget, op: int) -> Any:
        ... 


class IonIdentityMolecularNetworking:
    """
    Cython implementation of _IonIdentityMolecularNetworking

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1IonIdentityMolecularNetworking.html>`_

    Includes the necessary functions to generate filed required for GNPS ion identity molecular networking (IIMN).
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void IonIdentityMolecularNetworking()
        """
        ...
    
    annotateConsensusMap: __static_IonIdentityMolecularNetworking_annotateConsensusMap
    
    writeSupplementaryPairTable: __static_IonIdentityMolecularNetworking_writeSupplementaryPairTable 


class IsobaricChannelInformation:
    """
    Cython implementation of _IsobaricChannelInformation

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::IsobaricQuantitationMethod_1_1IsobaricChannelInformation.html>`_
    """
    
    name: Union[bytes, str, String]
    
    id: int
    
    description: Union[bytes, str, String]
    
    center: float
    
    affected_channels: List[int]
    
    @overload
    def __init__(self, name: Union[bytes, str, String] , id_: int , description: Union[bytes, str, String] , center: float , affected_channels: List[int] ) -> None:
        """
        Cython signature: void IsobaricChannelInformation(String name, int id_, String description, double center, libcpp_vector[int] affected_channels)
        """
        ...
    
    @overload
    def __init__(self, in_0: IsobaricChannelInformation ) -> None:
        """
        Cython signature: void IsobaricChannelInformation(IsobaricChannelInformation &)
        """
        ... 


class IsobaricQuantifier:
    """
    Cython implementation of _IsobaricQuantifier

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1IsobaricQuantifier.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, in_0: IsobaricQuantifier ) -> None:
        """
        Cython signature: void IsobaricQuantifier(IsobaricQuantifier &)
        """
        ...
    
    @overload
    def __init__(self, quant_method: ItraqFourPlexQuantitationMethod ) -> None:
        """
        Cython signature: void IsobaricQuantifier(ItraqFourPlexQuantitationMethod * quant_method)
        """
        ...
    
    @overload
    def __init__(self, quant_method: ItraqEightPlexQuantitationMethod ) -> None:
        """
        Cython signature: void IsobaricQuantifier(ItraqEightPlexQuantitationMethod * quant_method)
        """
        ...
    
    @overload
    def __init__(self, quant_method: TMTSixPlexQuantitationMethod ) -> None:
        """
        Cython signature: void IsobaricQuantifier(TMTSixPlexQuantitationMethod * quant_method)
        """
        ...
    
    @overload
    def __init__(self, quant_method: TMTTenPlexQuantitationMethod ) -> None:
        """
        Cython signature: void IsobaricQuantifier(TMTTenPlexQuantitationMethod * quant_method)
        """
        ...
    
    def quantify(self, consensus_map_in: ConsensusMap , consensus_map_out: ConsensusMap ) -> None:
        """
        Cython signature: void quantify(ConsensusMap & consensus_map_in, ConsensusMap & consensus_map_out)
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


class IsotopeCluster:
    """
    Cython implementation of _IsotopeCluster

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1IsotopeCluster.html>`_
    """
    
    peaks: ChargedIndexSet
    
    scans: List[int]
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void IsotopeCluster()
        Stores information about an isotopic cluster (i.e. potential peptide charge variants)
        """
        ...
    
    @overload
    def __init__(self, in_0: IsotopeCluster ) -> None:
        """
        Cython signature: void IsotopeCluster(IsotopeCluster &)
        """
        ... 


class IsotopeMarker:
    """
    Cython implementation of _IsotopeMarker

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1IsotopeMarker.html>`_
      -- Inherits from ['PeakMarker']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void IsotopeMarker()
        IsotopeMarker marks peak pairs which could represent an ion and its isotope
        """
        ...
    
    @overload
    def __init__(self, in_0: IsotopeMarker ) -> None:
        """
        Cython signature: void IsotopeMarker(IsotopeMarker &)
        """
        ...
    
    def apply(self, in_0: Dict[float, bool] , in_1: MSSpectrum ) -> None:
        """
        Cython signature: void apply(libcpp_map[double,bool] &, MSSpectrum &)
        """
        ...
    
    def getProductName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getProductName()
        Returns the product name
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


class ItraqFourPlexQuantitationMethod:
    """
    Cython implementation of _ItraqFourPlexQuantitationMethod

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ItraqFourPlexQuantitationMethod.html>`_
      -- Inherits from ['IsobaricQuantitationMethod']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ItraqFourPlexQuantitationMethod()
        iTRAQ 4 plex quantitation to be used with the IsobaricQuantitation
        """
        ...
    
    @overload
    def __init__(self, in_0: ItraqFourPlexQuantitationMethod ) -> None:
        """
        Cython signature: void ItraqFourPlexQuantitationMethod(ItraqFourPlexQuantitationMethod &)
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


class KDTreeFeatureNode:
    """
    Cython implementation of _KDTreeFeatureNode

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1KDTreeFeatureNode.html>`_
    """
    
    @overload
    def __init__(self, in_0: KDTreeFeatureNode ) -> None:
        """
        Cython signature: void KDTreeFeatureNode(KDTreeFeatureNode &)
        """
        ...
    
    @overload
    def __init__(self, data: KDTreeFeatureMaps , idx: int ) -> None:
        """
        Cython signature: void KDTreeFeatureNode(KDTreeFeatureMaps * data, size_t idx)
        """
        ...
    
    def __getitem__(self, i: int ) -> float:
        """
        Cython signature: double operator[](size_t i)
        """
        ...
    
    def getIndex(self) -> int:
        """
        Cython signature: size_t getIndex()
        Returns index of corresponding feature in data_
        """
        ... 


class Kernel_MassTrace:
    """
    Cython implementation of _Kernel_MassTrace

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1Kernel_MassTrace.html>`_
    """
    
    fwhm_mz_avg: float
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void Kernel_MassTrace()
        """
        ...
    
    @overload
    def __init__(self, in_0: Kernel_MassTrace ) -> None:
        """
        Cython signature: void Kernel_MassTrace(Kernel_MassTrace &)
        """
        ...
    
    @overload
    def __init__(self, trace_peaks: List[Peak2D] ) -> None:
        """
        Cython signature: void Kernel_MassTrace(const libcpp_vector[Peak2D] & trace_peaks)
        """
        ...
    
    def getSize(self) -> int:
        """
        Cython signature: size_t getSize()
        Returns the number of peaks contained in the mass trace
        """
        ...
    
    def getLabel(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getLabel()
        Returns label of mass trace
        """
        ...
    
    def setLabel(self, label: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setLabel(String label)
        Sets label of mass trace
        """
        ...
    
    def getCentroidMZ(self) -> float:
        """
        Cython signature: double getCentroidMZ()
        Returns the centroid m/z
        """
        ...
    
    def getCentroidRT(self) -> float:
        """
        Cython signature: double getCentroidRT()
        Returns the centroid RT
        """
        ...
    
    def getCentroidSD(self) -> float:
        """
        Cython signature: double getCentroidSD()
        Returns the centroid SD
        """
        ...
    
    def getFWHM(self) -> float:
        """
        Cython signature: double getFWHM()
        Returns FWHM
        """
        ...
    
    def getTraceLength(self) -> float:
        """
        Cython signature: double getTraceLength()
        Returns the length of the trace (as difference in RT)
        """
        ...
    
    def getFWHMborders(self) -> List[int, int]:
        """
        Cython signature: libcpp_pair[size_t,size_t] getFWHMborders()
        Returns FWHM boarders
        """
        ...
    
    def getSmoothedIntensities(self) -> List[float]:
        """
        Cython signature: libcpp_vector[double] getSmoothedIntensities()
        Returns smoothed intensities (empty if no smoothing was explicitly done beforehand!)
        """
        ...
    
    def getAverageMS1CycleTime(self) -> float:
        """
        Cython signature: double getAverageMS1CycleTime()
        Returns average scan time of mass trace
        """
        ...
    
    def computeSmoothedPeakArea(self) -> float:
        """
        Cython signature: double computeSmoothedPeakArea()
        Sums all non-negative (smoothed!) intensities in the mass trace
        """
        ...
    
    def computePeakArea(self) -> float:
        """
        Cython signature: double computePeakArea()
        Sums intensities of all peaks in the mass trace
        """
        ...
    
    def findMaxByIntPeak(self, in_0: bool ) -> int:
        """
        Cython signature: size_t findMaxByIntPeak(bool)
        Returns the index of the mass trace's highest peak within the MassTrace container (based either on raw or smoothed intensities)
        """
        ...
    
    def estimateFWHM(self, in_0: bool ) -> int:
        """
        Cython signature: size_t estimateFWHM(bool)
        Estimates FWHM of chromatographic peak in seconds (based on either raw or smoothed intensities)
        """
        ...
    
    def computeFwhmArea(self) -> float:
        """
        Cython signature: double computeFwhmArea()
        """
        ...
    
    def computeFwhmAreaSmooth(self) -> float:
        """
        Cython signature: double computeFwhmAreaSmooth()
        Computes chromatographic peak area within the FWHM range.
        """
        ...
    
    def getIntensity(self, in_0: bool ) -> float:
        """
        Cython signature: double getIntensity(bool)
        Returns the intensity
        """
        ...
    
    def getMaxIntensity(self, in_0: bool ) -> float:
        """
        Cython signature: double getMaxIntensity(bool)
        Returns the max intensity
        """
        ...
    
    def getConvexhull(self) -> ConvexHull2D:
        """
        Cython signature: ConvexHull2D getConvexhull()
        Returns the mass trace's convex hull
        """
        ...
    
    def setCentroidSD(self, tmp_sd: float ) -> None:
        """
        Cython signature: void setCentroidSD(double & tmp_sd)
        """
        ...
    
    def setSmoothedIntensities(self, db_vec: List[float] ) -> None:
        """
        Cython signature: void setSmoothedIntensities(libcpp_vector[double] & db_vec)
        Sets smoothed intensities (smoothing is done externally, e.g. by LowessSmoothing)
        """
        ...
    
    def updateSmoothedMaxRT(self) -> None:
        """
        Cython signature: void updateSmoothedMaxRT()
        """
        ...
    
    def updateWeightedMeanRT(self) -> None:
        """
        Cython signature: void updateWeightedMeanRT()
        Compute & update centroid RT as a intensity-weighted mean of RTs
        """
        ...
    
    def updateSmoothedWeightedMeanRT(self) -> None:
        """
        Cython signature: void updateSmoothedWeightedMeanRT()
        """
        ...
    
    def updateMedianRT(self) -> None:
        """
        Cython signature: void updateMedianRT()
        Compute & update centroid RT as median position of intensities
        """
        ...
    
    def updateMedianMZ(self) -> None:
        """
        Cython signature: void updateMedianMZ()
        Compute & update centroid m/z as median of m/z values
        """
        ...
    
    def updateMeanMZ(self) -> None:
        """
        Cython signature: void updateMeanMZ()
        Compute & update centroid m/z as mean of m/z values
        """
        ...
    
    def updateWeightedMeanMZ(self) -> None:
        """
        Cython signature: void updateWeightedMeanMZ()
        Compute & update centroid m/z as weighted mean of m/z values
        """
        ...
    
    def updateWeightedMZsd(self) -> None:
        """
        Cython signature: void updateWeightedMZsd()
        Compute & update m/z standard deviation of mass trace as weighted mean of m/z values
        
        Make sure to call update(Weighted)(Mean|Median)MZ() first! <br>
        use getCentroidSD() to get result
        """
        ...
    
    def setQuantMethod(self, method: int ) -> None:
        """
        Cython signature: void setQuantMethod(MT_QUANTMETHOD method)
        Determine if area or median is used for quantification
        """
        ...
    
    def getQuantMethod(self) -> int:
        """
        Cython signature: MT_QUANTMETHOD getQuantMethod()
        Check if area or median is used for quantification
        """
        ... 


class LinearInterpolation:
    """
    Cython implementation of _LinearInterpolation[double,double]

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::Math_1_1LinearInterpolation[double,double].html>`_

    Provides access to linearly interpolated values (and
    derivatives) from discrete data points.  Values beyond the given range
    of data points are implicitly taken as zero.
    
    The input is just a vector of values ("Data").  These are interpreted
    as the y-coordinates at the x-coordinate positions 0,...,data_.size-1.
    
    The interpolated data can also be scaled and shifted in
    the x-dimension by an affine mapping.  That is, we have "inside" and
    "outside" x-coordinates.  The affine mapping can be specified in two
    ways:
    - using setScale() and setOffset(),
    - using setMapping()
    
    By default the identity mapping (scale=1, offset=0) is used.
    
    Using the value() and derivative() methods you can sample linearly
    interpolated values for a given x-coordinate position of the data and
    the derivative of the data
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void LinearInterpolation()
        """
        ...
    
    @overload
    def __init__(self, in_0: LinearInterpolation ) -> None:
        """
        Cython signature: void LinearInterpolation(LinearInterpolation &)
        """
        ...
    
    @overload
    def __init__(self, scale: float , offset: float ) -> None:
        """
        Cython signature: void LinearInterpolation(double scale, double offset)
        """
        ...
    
    def value(self, arg_pos: float ) -> float:
        """
        Cython signature: double value(double arg_pos)
        Returns the interpolated value
        """
        ...
    
    def addValue(self, arg_pos: float , arg_value: float ) -> None:
        """
        Cython signature: void addValue(double arg_pos, double arg_value)
        Performs linear resampling. The `arg_value` is split up and added to the data points around `arg_pos`
        """
        ...
    
    def derivative(self, arg_pos: float ) -> float:
        """
        Cython signature: double derivative(double arg_pos)
        Returns the interpolated derivative
        """
        ...
    
    def getData(self) -> List[float]:
        """
        Cython signature: libcpp_vector[double] getData()
        Returns the internal random access container from which interpolated values are being sampled
        """
        ...
    
    def setData(self, data: List[float] ) -> None:
        """
        Cython signature: void setData(libcpp_vector[double] & data)
        Assigns data to the internal random access container from which interpolated values are being sampled
        """
        ...
    
    def empty(self) -> bool:
        """
        Cython signature: bool empty()
        Returns `true` if getData() is empty
        """
        ...
    
    def key2index(self, pos: float ) -> float:
        """
        Cython signature: double key2index(double pos)
        The transformation from "outside" to "inside" coordinates
        """
        ...
    
    def index2key(self, pos: float ) -> float:
        """
        Cython signature: double index2key(double pos)
        The transformation from "inside" to "outside" coordinates
        """
        ...
    
    def getScale(self) -> float:
        """
        Cython signature: double getScale()
        "Scale" is the difference (in "outside" units) between consecutive entries in "Data"
        """
        ...
    
    def setScale(self, scale: float ) -> None:
        """
        Cython signature: void setScale(double & scale)
        "Scale" is the difference (in "outside" units) between consecutive entries in "Data"
        """
        ...
    
    def getOffset(self) -> float:
        """
        Cython signature: double getOffset()
        "Offset" is the point (in "outside" units) which corresponds to "Data[0]"
        """
        ...
    
    def setOffset(self, offset: float ) -> None:
        """
        Cython signature: void setOffset(double & offset)
        "Offset" is the point (in "outside" units) which corresponds to "Data[0]"
        """
        ...
    
    @overload
    def setMapping(self, scale: float , inside: float , outside: float ) -> None:
        """
        Cython signature: void setMapping(double & scale, double & inside, double & outside)
        """
        ...
    
    @overload
    def setMapping(self, inside_low: float , outside_low: float , inside_high: float , outside_high: float ) -> None:
        """
        Cython signature: void setMapping(double & inside_low, double & outside_low, double & inside_high, double & outside_high)
        """
        ...
    
    def getInsideReferencePoint(self) -> float:
        """
        Cython signature: double getInsideReferencePoint()
        """
        ...
    
    def getOutsideReferencePoint(self) -> float:
        """
        Cython signature: double getOutsideReferencePoint()
        """
        ...
    
    def supportMin(self) -> float:
        """
        Cython signature: double supportMin()
        """
        ...
    
    def supportMax(self) -> float:
        """
        Cython signature: double supportMax()
        """
        ... 


class MRMFQC_ComponentGroupPairQCs:
    """
    Cython implementation of _MRMFQC_ComponentGroupPairQCs

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMFQC_ComponentGroupPairQCs.html>`_
    """
    
    component_group_name: Union[bytes, str, String]
    
    resolution_pair_name: Union[bytes, str, String]
    
    resolution_l: float
    
    resolution_u: float
    
    rt_diff_l: float
    
    rt_diff_u: float
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MRMFQC_ComponentGroupPairQCs()
        """
        ...
    
    @overload
    def __init__(self, in_0: MRMFQC_ComponentGroupPairQCs ) -> None:
        """
        Cython signature: void MRMFQC_ComponentGroupPairQCs(MRMFQC_ComponentGroupPairQCs &)
        """
        ... 


class MRMFQC_ComponentGroupQCs:
    """
    Cython implementation of _MRMFQC_ComponentGroupQCs

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMFQC_ComponentGroupQCs.html>`_
    """
    
    component_group_name: Union[bytes, str, String]
    
    retention_time_l: float
    
    retention_time_u: float
    
    intensity_l: float
    
    intensity_u: float
    
    overall_quality_l: float
    
    overall_quality_u: float
    
    n_heavy_l: int
    
    n_heavy_u: int
    
    n_light_l: int
    
    n_light_u: int
    
    n_detecting_l: int
    
    n_detecting_u: int
    
    n_quantifying_l: int
    
    n_quantifying_u: int
    
    n_identifying_l: int
    
    n_identifying_u: int
    
    n_transitions_l: int
    
    n_transitions_u: int
    
    ion_ratio_pair_name_1: Union[bytes, str, String]
    
    ion_ratio_pair_name_2: Union[bytes, str, String]
    
    ion_ratio_l: float
    
    ion_ratio_u: float
    
    ion_ratio_feature_name: Union[bytes, str, String]
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MRMFQC_ComponentGroupQCs()
        """
        ...
    
    @overload
    def __init__(self, in_0: MRMFQC_ComponentGroupQCs ) -> None:
        """
        Cython signature: void MRMFQC_ComponentGroupQCs(MRMFQC_ComponentGroupQCs &)
        """
        ... 


class MRMFQC_ComponentQCs:
    """
    Cython implementation of _MRMFQC_ComponentQCs

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMFQC_ComponentQCs.html>`_
    """
    
    component_name: Union[bytes, str, String]
    
    retention_time_l: float
    
    retention_time_u: float
    
    intensity_l: float
    
    intensity_u: float
    
    overall_quality_l: float
    
    overall_quality_u: float
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MRMFQC_ComponentQCs()
        """
        ...
    
    @overload
    def __init__(self, in_0: MRMFQC_ComponentQCs ) -> None:
        """
        Cython signature: void MRMFQC_ComponentQCs(MRMFQC_ComponentQCs &)
        """
        ... 


class MRMFeatureQC:
    """
    Cython implementation of _MRMFeatureQC

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMFeatureQC.html>`_
    """
    
    component_qcs: List[MRMFQC_ComponentQCs]
    
    component_group_qcs: List[MRMFQC_ComponentGroupQCs]
    
    component_group_pair_qcs: List[MRMFQC_ComponentGroupPairQCs]
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MRMFeatureQC()
        """
        ...
    
    @overload
    def __init__(self, in_0: MRMFeatureQC ) -> None:
        """
        Cython signature: void MRMFeatureQC(MRMFeatureQC &)
        """
        ... 


class MSDataAggregatingConsumer:
    """
    Cython implementation of _MSDataAggregatingConsumer

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSDataAggregatingConsumer.html>`_
    """
    
    def __init__(self, in_0: MSDataAggregatingConsumer ) -> None:
        """
        Cython signature: void MSDataAggregatingConsumer(MSDataAggregatingConsumer &)
        """
        ...
    
    def consumeSpectrum(self, s: MSSpectrum ) -> None:
        """
        Cython signature: void consumeSpectrum(MSSpectrum & s)
        """
        ...
    
    def consumeChromatogram(self, in_0: MSChromatogram ) -> None:
        """
        Cython signature: void consumeChromatogram(MSChromatogram &)
        """
        ...
    
    def setExpectedSize(self, expectedSpectra: int , expectedChromatograms: int ) -> None:
        """
        Cython signature: void setExpectedSize(size_t expectedSpectra, size_t expectedChromatograms)
        """
        ...
    
    def setExperimentalSettings(self, exp: ExperimentalSettings ) -> None:
        """
        Cython signature: void setExperimentalSettings(ExperimentalSettings & exp)
        """
        ... 


class MSQuantifications:
    """
    Cython implementation of _MSQuantifications

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSQuantifications.html>`_
      -- Inherits from ['ExperimentalSettings']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MSQuantifications()
        """
        ...
    
    @overload
    def __init__(self, in_0: MSQuantifications ) -> None:
        """
        Cython signature: void MSQuantifications(MSQuantifications &)
        """
        ...
    
    @overload
    def __init__(self, fm: FeatureMap , es: ExperimentalSettings , dps: List[DataProcessing] ) -> None:
        """
        Cython signature: void MSQuantifications(FeatureMap fm, ExperimentalSettings & es, libcpp_vector[DataProcessing] & dps)
        """
        ...
    
    def getDataProcessingList(self) -> List[DataProcessing]:
        """
        Cython signature: libcpp_vector[DataProcessing] getDataProcessingList()
        """
        ...
    
    def getAssays(self) -> List[Assay]:
        """
        Cython signature: libcpp_vector[Assay] getAssays()
        """
        ...
    
    def getConsensusMaps(self) -> List[ConsensusMap]:
        """
        Cython signature: libcpp_vector[ConsensusMap] getConsensusMaps()
        """
        ...
    
    def setConsensusMaps(self, in_0: List[ConsensusMap] ) -> None:
        """
        Cython signature: void setConsensusMaps(libcpp_vector[ConsensusMap])
        """
        ...
    
    def getFeatureMaps(self) -> List[FeatureMap]:
        """
        Cython signature: libcpp_vector[FeatureMap] getFeatureMaps()
        """
        ...
    
    def getAnalysisSummary(self) -> AnalysisSummary:
        """
        Cython signature: AnalysisSummary getAnalysisSummary()
        """
        ...
    
    def setDataProcessingList(self, dpl: List[DataProcessing] ) -> None:
        """
        Cython signature: void setDataProcessingList(libcpp_vector[DataProcessing] dpl)
        """
        ...
    
    def setAnalysisSummaryQuantType(self, r: int ) -> None:
        """
        Cython signature: void setAnalysisSummaryQuantType(QUANT_TYPES r)
        """
        ...
    
    def addConsensusMap(self, m: ConsensusMap ) -> None:
        """
        Cython signature: void addConsensusMap(ConsensusMap m)
        """
        ...
    
    def assignUIDs(self) -> None:
        """
        Cython signature: void assignUIDs()
        """
        ...
    
    def getSourceFiles(self) -> List[SourceFile]:
        """
        Cython signature: libcpp_vector[SourceFile] getSourceFiles()
        Returns a reference to the source data file
        """
        ...
    
    def setSourceFiles(self, source_files: List[SourceFile] ) -> None:
        """
        Cython signature: void setSourceFiles(libcpp_vector[SourceFile] source_files)
        Sets the source data file
        """
        ...
    
    def getDateTime(self) -> DateTime:
        """
        Cython signature: DateTime getDateTime()
        Returns the date the experiment was performed
        """
        ...
    
    def setDateTime(self, date_time: DateTime ) -> None:
        """
        Cython signature: void setDateTime(DateTime date_time)
        Sets the date the experiment was performed
        """
        ...
    
    def getSample(self) -> Sample:
        """
        Cython signature: Sample getSample()
        Returns a reference to the sample description
        """
        ...
    
    def setSample(self, sample: Sample ) -> None:
        """
        Cython signature: void setSample(Sample sample)
        Sets the sample description
        """
        ...
    
    def getContacts(self) -> List[ContactPerson]:
        """
        Cython signature: libcpp_vector[ContactPerson] getContacts()
        Returns a reference to the list of contact persons
        """
        ...
    
    def setContacts(self, contacts: List[ContactPerson] ) -> None:
        """
        Cython signature: void setContacts(libcpp_vector[ContactPerson] contacts)
        Sets the list of contact persons
        """
        ...
    
    def getInstrument(self) -> Instrument:
        """
        Cython signature: Instrument getInstrument()
        Returns a reference to the MS instrument description
        """
        ...
    
    def setInstrument(self, instrument: Instrument ) -> None:
        """
        Cython signature: void setInstrument(Instrument instrument)
        Sets the MS instrument description
        """
        ...
    
    def getHPLC(self) -> HPLC:
        """
        Cython signature: HPLC getHPLC()
        Returns a reference to the description of the HPLC run
        """
        ...
    
    def setHPLC(self, hplc: HPLC ) -> None:
        """
        Cython signature: void setHPLC(HPLC hplc)
        Sets the description of the HPLC run
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
    
    def getProteinIdentifications(self) -> List[ProteinIdentification]:
        """
        Cython signature: libcpp_vector[ProteinIdentification] getProteinIdentifications()
        Returns a reference to the protein ProteinIdentification vector
        """
        ...
    
    def setProteinIdentifications(self, protein_identifications: List[ProteinIdentification] ) -> None:
        """
        Cython signature: void setProteinIdentifications(libcpp_vector[ProteinIdentification] protein_identifications)
        Sets the protein ProteinIdentification vector
        """
        ...
    
    def getFractionIdentifier(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getFractionIdentifier()
        Returns fraction identifier
        """
        ...
    
    def setFractionIdentifier(self, fraction_identifier: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setFractionIdentifier(String fraction_identifier)
        Sets the fraction identifier
        """
        ...
    
    def setIdentifier(self, id: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setIdentifier(String id)
        Sets document identifier (e.g. an LSID)
        """
        ...
    
    def getIdentifier(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getIdentifier()
        Retrieve document identifier (e.g. an LSID)
        """
        ...
    
    def setLoadedFileType(self, file_name: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setLoadedFileType(String file_name)
        Sets the file_type according to the type of the file loaded from, preferably done whilst loading
        """
        ...
    
    def getLoadedFileType(self) -> int:
        """
        Cython signature: int getLoadedFileType()
        Returns the file_type (e.g. featureXML, consensusXML, mzData, mzXML, mzML, ...) of the file loaded
        """
        ...
    
    def setLoadedFilePath(self, file_name: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setLoadedFilePath(String file_name)
        Sets the file_name according to absolute path of the file loaded, preferably done whilst loading
        """
        ...
    
    def getLoadedFilePath(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getLoadedFilePath()
        Returns the file_name which is the absolute path to the file loaded
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
    
    def __richcmp__(self, other: MSQuantifications, op: int) -> Any:
        ...
    QUANT_TYPES : __QUANT_TYPES 


class MSstatsFile:
    """
    Cython implementation of _MSstatsFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSstatsFile.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MSstatsFile()
        """
        ...
    
    @overload
    def __init__(self, in_0: MSstatsFile ) -> None:
        """
        Cython signature: void MSstatsFile(MSstatsFile &)
        """
        ...
    
    def storeLFQ(self, filename: String , consensus_map: ConsensusMap , design: ExperimentalDesign , reannotate_filenames: List[bytes] , is_isotope_label_type: bool , bioreplicate: String , condition: String , retention_time_summarization_method: String ) -> None:
        """
        Cython signature: void storeLFQ(String & filename, ConsensusMap & consensus_map, ExperimentalDesign & design, StringList & reannotate_filenames, bool is_isotope_label_type, String & bioreplicate, String & condition, String & retention_time_summarization_method)
        Store label free experiment (MSstats)
        """
        ...
    
    def storeISO(self, filename: String , consensus_map: ConsensusMap , design: ExperimentalDesign , reannotate_filenames: List[bytes] , bioreplicate: String , condition: String , mixture: String , retention_time_summarization_method: String ) -> None:
        """
        Cython signature: void storeISO(String & filename, ConsensusMap & consensus_map, ExperimentalDesign & design, StringList & reannotate_filenames, String & bioreplicate, String & condition, String & mixture, String & retention_time_summarization_method)
        Store isobaric experiment (MSstatsTMT)
        """
        ... 


class MapAlignmentEvaluationAlgorithmRecall:
    """
    Cython implementation of _MapAlignmentEvaluationAlgorithmRecall

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MapAlignmentEvaluationAlgorithmRecall.html>`_
      -- Inherits from ['MapAlignmentEvaluationAlgorithm']
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void MapAlignmentEvaluationAlgorithmRecall()
        """
        ...
    
    def getProductName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getProductName()
        Returns the product name (for the Factory)
        """
        ...
    
    def registerChildren(self) -> None:
        """
        Cython signature: void registerChildren()
        Register all derived classes in this method
        """
        ... 


class MassTraceDetection:
    """
    Cython implementation of _MassTraceDetection

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MassTraceDetection.html>`_
      -- Inherits from ['ProgressLogger', 'DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MassTraceDetection()
        """
        ...
    
    @overload
    def __init__(self, in_0: MassTraceDetection ) -> None:
        """
        Cython signature: void MassTraceDetection(MassTraceDetection &)
        """
        ...
    
    def run(self, input_map: MSExperiment , traces: List[Kernel_MassTrace] , max_traces: int ) -> None:
        """
        Cython signature: void run(MSExperiment & input_map, libcpp_vector[Kernel_MassTrace] & traces, size_t max_traces)
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


class MatrixDouble:
    """
    Cython implementation of _Matrix[double]

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1Matrix[double].html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MatrixDouble()
        """
        ...
    
    @overload
    def __init__(self, in_0: MatrixDouble ) -> None:
        """
        Cython signature: void MatrixDouble(MatrixDouble)
        """
        ...
    
    @overload
    def __init__(self, rows: int , cols: int , value: float ) -> None:
        """
        Cython signature: void MatrixDouble(size_t rows, size_t cols, double value)
        """
        ...
    
    def getValue(self, i: int , j: int ) -> float:
        """
        Cython signature: double getValue(size_t i, size_t j)
        """
        ...
    
    def setValue(self, i: int , j: int , value: float ) -> None:
        """
        Cython signature: void setValue(size_t i, size_t j, double value)
        """
        ...
    
    def clear(self) -> None:
        """
        Cython signature: void clear()
        """
        ...
    
    @overload
    def resize(self, i: int , j: int , value: float ) -> None:
        """
        Cython signature: void resize(size_t i, size_t j, double value)
        """
        ...
    
    @overload
    def resize(self, size_pair: List[int, int] , value: float ) -> None:
        """
        Cython signature: void resize(libcpp_pair[size_t,size_t] & size_pair, double value)
        """
        ...
    
    def rows(self) -> int:
        """
        Cython signature: size_t rows()
        """
        ...
    
    def cols(self) -> int:
        """
        Cython signature: size_t cols()
        """
        ...
    
    def sizePair(self) -> List[int, int]:
        """
        Cython signature: libcpp_pair[size_t,size_t] sizePair()
        """
        ...
    
    def index(self, row: int , col: int ) -> int:
        """
        Cython signature: size_t index(size_t row, size_t col)
        """
        ...
    
    def indexPair(self, index: int ) -> List[int, int]:
        """
        Cython signature: libcpp_pair[size_t,size_t] indexPair(size_t index)
        """
        ...
    
    def colIndex(self, index: int ) -> int:
        """
        Cython signature: size_t colIndex(size_t index)
        Calculate the column from an index into the underlying vector. Note that Matrix uses the (row,column) lexicographic ordering for indexing
        """
        ...
    
    def rowIndex(self, index: int ) -> int:
        """
        Cython signature: size_t rowIndex(size_t index)
        Calculate the row from an index into the underlying vector. Note that Matrix uses the (row,column) lexicographic ordering for indexing
        """
        ... 


class MultiplexIsotopicPeakPattern:
    """
    Cython implementation of _MultiplexIsotopicPeakPattern

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MultiplexIsotopicPeakPattern.html>`_
    """
    
    @overload
    def __init__(self, c: int , ppp: int , ms: MultiplexDeltaMasses , msi: int ) -> None:
        """
        Cython signature: void MultiplexIsotopicPeakPattern(int c, int ppp, MultiplexDeltaMasses ms, int msi)
        """
        ...
    
    @overload
    def __init__(self, in_0: MultiplexIsotopicPeakPattern ) -> None:
        """
        Cython signature: void MultiplexIsotopicPeakPattern(MultiplexIsotopicPeakPattern &)
        """
        ...
    
    def getCharge(self) -> int:
        """
        Cython signature: int getCharge()
        Returns charge
        """
        ...
    
    def getPeaksPerPeptide(self) -> int:
        """
        Cython signature: int getPeaksPerPeptide()
        Returns peaks per peptide
        """
        ...
    
    def getMassShifts(self) -> MultiplexDeltaMasses:
        """
        Cython signature: MultiplexDeltaMasses getMassShifts()
        Returns mass shifts
        """
        ...
    
    def getMassShiftIndex(self) -> int:
        """
        Cython signature: int getMassShiftIndex()
        Returns mass shift index
        """
        ...
    
    def getMassShiftCount(self) -> int:
        """
        Cython signature: unsigned int getMassShiftCount()
        Returns number of mass shifts i.e. the number of peptides in the multiplet
        """
        ...
    
    def getMassShiftAt(self, i: int ) -> float:
        """
        Cython signature: double getMassShiftAt(int i)
        Returns mass shift at position i
        """
        ...
    
    def getMZShiftAt(self, i: int ) -> float:
        """
        Cython signature: double getMZShiftAt(int i)
        Returns m/z shift at position i
        """
        ...
    
    def getMZShiftCount(self) -> int:
        """
        Cython signature: unsigned int getMZShiftCount()
        Returns number of m/z shifts
        """
        ... 


class MzDataFile:
    """
    Cython implementation of _MzDataFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MzDataFile.html>`_
      -- Inherits from ['ProgressLogger']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MzDataFile()
        File adapter for MzData files
        """
        ...
    
    @overload
    def __init__(self, in_0: MzDataFile ) -> None:
        """
        Cython signature: void MzDataFile(MzDataFile &)
        """
        ...
    
    def load(self, filename: Union[bytes, str, String] , map: MSExperiment ) -> None:
        """
        Cython signature: void load(const String & filename, MSExperiment & map)
        Loads a map from a MzData file
        
        
        :param filename: Directory of the file with the file name
        :param map: It has to be a MSExperiment or have the same interface
        :raises:
          Exception: FileNotFound is thrown if the file could not be opened
        :raises:
          Exception: ParseError is thrown if an error occurs during parsing
        """
        ...
    
    def store(self, filename: Union[bytes, str, String] , map: MSExperiment ) -> None:
        """
        Cython signature: void store(const String & filename, MSExperiment & map)
        Stores a map in a MzData file
        
        
        :param filename: Directory of the file with the file name
        :param map: It has to be a MSExperiment or have the same interface
        :raises:
          Exception: UnableToCreateFile is thrown if the file could not be created
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
    
    def isSemanticallyValid(self, filename: Union[bytes, str, String] , errors: List[bytes] , warnings: List[bytes] ) -> bool:
        """
        Cython signature: bool isSemanticallyValid(const String & filename, StringList & errors, StringList & warnings)
        Checks if a file is valid with respect to the mapping file and the controlled vocabulary
        
        
        :param filename: File name of the file to be checked
        :param errors: Errors during the validation are returned in this output parameter
        :param warnings: Warnings during the validation are returned in this output parameter
        :raises:
          Exception: FileNotFound is thrown if the file could not be opened
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


class MzMLSqliteHandler:
    """
    Cython implementation of _MzMLSqliteHandler

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::Internal_1_1MzMLSqliteHandler.html>`_
    """
    
    @overload
    def __init__(self, filename: Union[bytes, str, String] , run_id: int ) -> None:
        """
        Cython signature: void MzMLSqliteHandler(String filename, uint64_t run_id)
        """
        ...
    
    @overload
    def __init__(self, in_0: MzMLSqliteHandler ) -> None:
        """
        Cython signature: void MzMLSqliteHandler(MzMLSqliteHandler &)
        """
        ...
    
    def readExperiment(self, exp: MSExperiment , meta_only: bool ) -> None:
        """
        Cython signature: void readExperiment(MSExperiment & exp, bool meta_only)
        Read an experiment into an MSExperiment structure
        
        
        :param exp: The result data structure
        :param meta_only: Only read the meta data
        """
        ...
    
    def readSpectra(self, exp: List[MSSpectrum] , indices: List[int] , meta_only: bool ) -> None:
        """
        Cython signature: void readSpectra(libcpp_vector[MSSpectrum] & exp, libcpp_vector[int] indices, bool meta_only)
        Read a set of spectra (potentially restricted to a subset)
        
        
        :param exp: The result data structure
        :param indices: A list of indices restricting the resulting spectra only to those specified here
        :param meta_only: Only read the meta data
        """
        ...
    
    def readChromatograms(self, exp: List[MSChromatogram] , indices: List[int] , meta_only: bool ) -> None:
        """
        Cython signature: void readChromatograms(libcpp_vector[MSChromatogram] & exp, libcpp_vector[int] indices, bool meta_only)
        Read a set of chromatograms (potentially restricted to a subset)
        
        
        :param exp: The result data structure
        :param indices: A list of indices restricting the resulting spectra only to those specified here
        :param meta_only: Only read the meta data
        """
        ...
    
    def getNrSpectra(self) -> int:
        """
        Cython signature: size_t getNrSpectra()
        Returns number of spectra in the file, reutrns the number of spectra
        """
        ...
    
    def getNrChromatograms(self) -> int:
        """
        Cython signature: size_t getNrChromatograms()
        Returns the number of chromatograms in the file
        """
        ...
    
    def setConfig(self, write_full_meta: bool , use_lossy_compression: bool , linear_abs_mass_acc: float ) -> None:
        """
        Cython signature: void setConfig(bool write_full_meta, bool use_lossy_compression, double linear_abs_mass_acc)
        Sets file configuration
        
        
        :param write_full_meta: Whether to write a complete mzML meta data structure into the RUN_EXTRA field (allows complete recovery of the input file)
        :param use_lossy_compression: Whether to use lossy compression (ms numpress)
        :param linear_abs_mass_acc: Accepted loss in mass accuracy (absolute m/z, in Th)
        """
        ...
    
    def getSpectraIndicesbyRT(self, RT: float , deltaRT: float , indices: List[int] ) -> List[int]:
        """
        Cython signature: libcpp_vector[size_t] getSpectraIndicesbyRT(double RT, double deltaRT, libcpp_vector[int] indices)
        Returns spectral indices around a specific retention time
        
        :param RT: The retention time
        :param deltaRT: Tolerance window around RT (if less or equal than zero, only the first spectrum *after* RT is returned)
        :param indices: Spectra to consider (if empty, all spectra are considered)
        :return: The indices of the spectra within RT +/- deltaRT
        """
        ...
    
    def writeExperiment(self, exp: MSExperiment ) -> None:
        """
        Cython signature: void writeExperiment(MSExperiment exp)
        Write an MSExperiment to disk
        """
        ...
    
    def createTables(self) -> None:
        """
        Cython signature: void createTables()
        Create data tables for a new file
        """
        ...
    
    def writeSpectra(self, spectra: List[MSSpectrum] ) -> None:
        """
        Cython signature: void writeSpectra(libcpp_vector[MSSpectrum] spectra)
        Writes a set of spectra to disk
        """
        ...
    
    def writeChromatograms(self, chroms: List[MSChromatogram] ) -> None:
        """
        Cython signature: void writeChromatograms(libcpp_vector[MSChromatogram] chroms)
        Writes a set of chromatograms to disk
        """
        ...
    
    def writeRunLevelInformation(self, exp: MSExperiment , write_full_meta: bool ) -> None:
        """
        Cython signature: void writeRunLevelInformation(MSExperiment exp, bool write_full_meta)
        Write the run-level information for an experiment into tables
        
        This is a low level function, do not call this function unless you know what you are doing
        
        
        :param exp: The result data structure
        :param meta_only: Only read the meta data
        """
        ...
    
    def getRunID(self) -> int:
        """
        Cython signature: uint64_t getRunID()
        Extract the `RUN` ID from the sqMass file
        """
        ... 


class NLargest:
    """
    Cython implementation of _NLargest

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1NLargest.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void NLargest()
        """
        ...
    
    @overload
    def __init__(self, in_0: NLargest ) -> None:
        """
        Cython signature: void NLargest(NLargest &)
        """
        ...
    
    def filterSpectrum(self, spec: MSSpectrum ) -> None:
        """
        Cython signature: void filterSpectrum(MSSpectrum & spec)
        Keep only n-largest peaks in spectrum
        """
        ...
    
    def filterPeakSpectrum(self, spec: MSSpectrum ) -> None:
        """
        Cython signature: void filterPeakSpectrum(MSSpectrum & spec)
        Keep only n-largest peaks in spectrum
        """
        ...
    
    def filterPeakMap(self, exp: MSExperiment ) -> None:
        """
        Cython signature: void filterPeakMap(MSExperiment & exp)
        Keep only n-largest peaks in each spectrum of a peak map
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


class NoopMSDataWritingConsumer:
    """
    Cython implementation of _NoopMSDataWritingConsumer

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1NoopMSDataWritingConsumer.html>`_

    Consumer class that perform no operation
    
    This is sometimes necessary to fulfill the requirement of passing an
    valid MSDataWritingConsumer object or pointer but no operation is
    required
    """
    
    def __init__(self, filename: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void NoopMSDataWritingConsumer(String filename)
        """
        ...
    
    def consumeSpectrum(self, s: MSSpectrum ) -> None:
        """
        Cython signature: void consumeSpectrum(MSSpectrum & s)
        """
        ...
    
    def consumeChromatogram(self, c: MSChromatogram ) -> None:
        """
        Cython signature: void consumeChromatogram(MSChromatogram & c)
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
    
    def addDataProcessing(self, d: DataProcessing ) -> None:
        """
        Cython signature: void addDataProcessing(DataProcessing d)
        """
        ...
    
    def getNrSpectraWritten(self) -> int:
        """
        Cython signature: size_t getNrSpectraWritten()
        """
        ...
    
    def getNrChromatogramsWritten(self) -> int:
        """
        Cython signature: size_t getNrChromatogramsWritten()
        """
        ... 


class OPXLDataStructs:
    """
    Cython implementation of _OPXLDataStructs

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1OPXLDataStructs.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void OPXLDataStructs()
        """
        ...
    
    @overload
    def __init__(self, in_0: OPXLDataStructs ) -> None:
        """
        Cython signature: void OPXLDataStructs(OPXLDataStructs &)
        """
        ...
    PeptidePosition : __PeptidePosition
    ProteinProteinCrossLinkType : __ProteinProteinCrossLinkType 


class OSBinaryDataArray:
    """
    Cython implementation of _OSBinaryDataArray

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenSwath_1_1OSBinaryDataArray.html>`_
    """
    
    data: List[float]
    
    description: bytes
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void OSBinaryDataArray()
        """
        ...
    
    @overload
    def __init__(self, in_0: OSBinaryDataArray ) -> None:
        """
        Cython signature: void OSBinaryDataArray(OSBinaryDataArray &)
        """
        ... 


class OSChromatogram:
    """
    Cython implementation of _OSChromatogram

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenSwath_1_1OSChromatogram.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void OSChromatogram()
        """
        ...
    
    @overload
    def __init__(self, in_0: OSChromatogram ) -> None:
        """
        Cython signature: void OSChromatogram(OSChromatogram &)
        """
        ... 


class OSSpectrum:
    """
    Cython implementation of _OSSpectrum

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenSwath_1_1OSSpectrum.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void OSSpectrum()
        """
        ...
    
    @overload
    def __init__(self, in_0: OSSpectrum ) -> None:
        """
        Cython signature: void OSSpectrum(OSSpectrum &)
        """
        ... 


class PeakCandidate:
    """
    Cython implementation of _PeakCandidate

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakCandidate.html>`_
    """
    
    pos: int
    
    left_boundary: int
    
    right_boundary: int
    
    mz_max: float
    
    int_max: float
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void PeakCandidate()
        """
        ...
    
    @overload
    def __init__(self, in_0: PeakCandidate ) -> None:
        """
        Cython signature: void PeakCandidate(PeakCandidate &)
        """
        ... 


class PeakPickerMRM:
    """
    Cython implementation of _PeakPickerMRM

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakPickerMRM.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void PeakPickerMRM()
        """
        ...
    
    @overload
    def __init__(self, in_0: PeakPickerMRM ) -> None:
        """
        Cython signature: void PeakPickerMRM(PeakPickerMRM &)
        """
        ...
    
    def pickChromatogram(self, chromatogram: MSChromatogram , picked_chrom: MSChromatogram ) -> None:
        """
        Cython signature: void pickChromatogram(MSChromatogram & chromatogram, MSChromatogram & picked_chrom)
        Finds peaks in a single chromatogram and annotates left/right borders
        
        It uses a modified algorithm of the PeakPickerHiRes
        
        This function will return a picked chromatogram
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


class PeakPickerMaxima:
    """
    Cython implementation of _PeakPickerMaxima

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakPickerMaxima.html>`_

    This class implements a fast peak-picking algorithm best suited for
    high resolution MS data (FT-ICR-MS, Orbitrap). In high resolution data, the
    signals of ions with similar mass-to-charge ratios (m/z) exhibit little or
    no overlapping and therefore allow for a clear separation. Furthermore, ion
    signals tend to show well-defined peak shapes with narrow peak width
    
    This peak-picking algorithm detects ion signals in raw data and
    reconstructs the corresponding peak shape by cubic spline interpolation.
    Signal detection depends on the signal-to-noise ratio which is adjustable
    by the user (see parameter signal_to_noise). A picked peak's m/z and
    intensity value is given by the maximum of the underlying peak spline
    
    So far, this peak picker was mainly tested on high resolution data. With
    appropriate preprocessing steps (e.g. noise reduction and baseline
    subtraction), it might be also applied to low resolution data
    """
    
    @overload
    def __init__(self, signal_to_noise: float , spacing_difference: float , sn_window_length: float ) -> None:
        """
        Cython signature: void PeakPickerMaxima(double signal_to_noise, double spacing_difference, double sn_window_length)
        """
        ...
    
    @overload
    def __init__(self, in_0: PeakPickerMaxima ) -> None:
        """
        Cython signature: void PeakPickerMaxima(PeakPickerMaxima &)
        """
        ...
    
    def findMaxima(self, mz_array: List[float] , int_array: List[float] , pc: List[PeakCandidate] ) -> None:
        """
        Cython signature: void findMaxima(libcpp_vector[double] mz_array, libcpp_vector[double] int_array, libcpp_vector[PeakCandidate] & pc)
        Will find local maxima in raw data
        
        
        :param mz_array: The array containing m/z values
        :param int_array: The array containing intensity values
        :param pc: The resulting array containing the peak candidates
        :param check_spacings: Check spacing constraints (recommended settings: yes for spectra, no for chromatograms)
        """
        ...
    
    def pick(self, mz_array: List[float] , int_array: List[float] , pc: List[PeakCandidate] ) -> None:
        """
        Cython signature: void pick(libcpp_vector[double] mz_array, libcpp_vector[double] int_array, libcpp_vector[PeakCandidate] & pc)
        """
        ... 


class PeptideIndexing:
    """
    Cython implementation of _PeptideIndexing

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeptideIndexing.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void PeptideIndexing()
        """
        ...
    
    @overload
    def __init__(self, in_0: PeptideIndexing ) -> None:
        """
        Cython signature: void PeptideIndexing(PeptideIndexing &)
        """
        ...
    
    def run(self, proteins: List[FASTAEntry] , prot_ids: List[ProteinIdentification] , pep_ids: List[PeptideIdentification] ) -> int:
        """
        Cython signature: PeptideIndexing_ExitCodes run(libcpp_vector[FASTAEntry] & proteins, libcpp_vector[ProteinIdentification] & prot_ids, libcpp_vector[PeptideIdentification] & pep_ids)
        """
        ...
    
    def getDecoyString(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getDecoyString()
        """
        ...
    
    def isPrefix(self) -> bool:
        """
        Cython signature: bool isPrefix()
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
    PeptideIndexing_ExitCodes : __PeptideIndexing_ExitCodes 


class PlainMSDataWritingConsumer:
    """
    Cython implementation of _PlainMSDataWritingConsumer

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PlainMSDataWritingConsumer.html>`_
    """
    
    def __init__(self, filename: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void PlainMSDataWritingConsumer(String filename)
        """
        ...
    
    def consumeSpectrum(self, s: MSSpectrum ) -> None:
        """
        Cython signature: void consumeSpectrum(MSSpectrum & s)
        """
        ...
    
    def consumeChromatogram(self, c: MSChromatogram ) -> None:
        """
        Cython signature: void consumeChromatogram(MSChromatogram & c)
        """
        ...
    
    def setExperimentalSettings(self, exp: ExperimentalSettings ) -> None:
        """
        Cython signature: void setExperimentalSettings(ExperimentalSettings & exp)
        Set experimental settings for the whole file
        
        
        :param exp: Experimental settings to be used for this file (from this and the first spectrum/chromatogram, the class will deduce most of the header of the mzML file)
        """
        ...
    
    def setExpectedSize(self, expectedSpectra: int , expectedChromatograms: int ) -> None:
        """
        Cython signature: void setExpectedSize(size_t expectedSpectra, size_t expectedChromatograms)
        Set expected size of spectra and chromatograms to be written
        
        These numbers will be written in the spectrumList and chromatogramList
        tag in the mzML file. Therefore, these will contain wrong numbers if
        the expected size is not set correctly
        
        
        :param expectedSpectra: Number of spectra expected
        :param expectedChromatograms: Number of chromatograms expected
        """
        ...
    
    def addDataProcessing(self, d: DataProcessing ) -> None:
        """
        Cython signature: void addDataProcessing(DataProcessing d)
        Optionally add a data processing method to each chromatogram and spectrum
        
        The provided DataProcessing object will be added to each chromatogram
        and spectrum written to to the mzML file
        
        
        :param d: The DataProcessing object to be added
        """
        ...
    
    def getNrSpectraWritten(self) -> int:
        """
        Cython signature: size_t getNrSpectraWritten()
        Returns the number of spectra written
        """
        ...
    
    def getNrChromatogramsWritten(self) -> int:
        """
        Cython signature: size_t getNrChromatogramsWritten()
        Returns the number of chromatograms written
        """
        ...
    
    def setOptions(self, opt: PeakFileOptions ) -> None:
        """
        Cython signature: void setOptions(PeakFileOptions opt)
        """
        ...
    
    def getOptions(self) -> PeakFileOptions:
        """
        Cython signature: PeakFileOptions getOptions()
        """
        ... 


class ProbablePhosphoSites:
    """
    Cython implementation of _ProbablePhosphoSites

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ProbablePhosphoSites.html>`_
    """
    
    first: int
    
    second: int
    
    seq_1: int
    
    seq_2: int
    
    peak_depth: int
    
    AScore: int
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ProbablePhosphoSites()
        """
        ...
    
    @overload
    def __init__(self, in_0: ProbablePhosphoSites ) -> None:
        """
        Cython signature: void ProbablePhosphoSites(ProbablePhosphoSites &)
        """
        ... 


class ProgressLogger:
    """
    Cython implementation of _ProgressLogger

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ProgressLogger.html>`_

    Base class for all classes that want to report their progress
    
    Per default the progress log is disabled. Use setLogType to enable it
    
    Use startProgress, setProgress and endProgress for the actual logging
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ProgressLogger()
        """
        ...
    
    @overload
    def __init__(self, in_0: ProgressLogger ) -> None:
        """
        Cython signature: void ProgressLogger(ProgressLogger &)
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


class ProteaseDB:
    """
    Cython implementation of _ProteaseDB

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ProteaseDB.html>`_
    """
    
    def getEnzyme(self, name: Union[bytes, str, String] ) -> DigestionEnzymeProtein:
        """
        Cython signature: const DigestionEnzymeProtein * getEnzyme(const String & name)
        """
        ...
    
    def getEnzymeByRegEx(self, cleavage_regex: Union[bytes, str, String] ) -> DigestionEnzymeProtein:
        """
        Cython signature: const DigestionEnzymeProtein * getEnzymeByRegEx(const String & cleavage_regex)
        """
        ...
    
    def getAllNames(self, all_names: List[bytes] ) -> None:
        """
        Cython signature: void getAllNames(libcpp_vector[String] & all_names)
        """
        ...
    
    def getAllXTandemNames(self, all_names: List[bytes] ) -> None:
        """
        Cython signature: void getAllXTandemNames(libcpp_vector[String] & all_names)
        Returns all the enzyme names available for XTandem
        """
        ...
    
    def getAllOMSSANames(self, all_names: List[bytes] ) -> None:
        """
        Cython signature: void getAllOMSSANames(libcpp_vector[String] & all_names)
        Returns all the enzyme names available for OMSSA
        """
        ...
    
    def getAllCometNames(self, all_names: List[bytes] ) -> None:
        """
        Cython signature: void getAllCometNames(libcpp_vector[String] & all_names)
        Returns all the enzyme names available for Comet
        """
        ...
    
    def getAllMSGFNames(self, all_names: List[bytes] ) -> None:
        """
        Cython signature: void getAllMSGFNames(libcpp_vector[String] & all_names)
        Returns all the enzyme names available for MSGFPlus
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


class RansacModelLinear:
    """
    Cython implementation of _RansacModelLinear

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::Math_1_1RansacModelLinear.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void RansacModelLinear()
        """
        ...
    
    @overload
    def __init__(self, in_0: RansacModelLinear ) -> None:
        """
        Cython signature: void RansacModelLinear(RansacModelLinear &)
        """
        ... 


class RealMassDecomposer:
    """
    Cython implementation of _RealMassDecomposer

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::ims_1_1RealMassDecomposer.html>`_
    """
    
    @overload
    def __init__(self, in_0: RealMassDecomposer ) -> None:
        """
        Cython signature: void RealMassDecomposer(RealMassDecomposer)
        """
        ...
    
    @overload
    def __init__(self, weights: IMSWeights ) -> None:
        """
        Cython signature: void RealMassDecomposer(IMSWeights & weights)
        """
        ...
    
    def getNumberOfDecompositions(self, mass: float , error: float ) -> int:
        """
        Cython signature: uint64_t getNumberOfDecompositions(double mass, double error)
        Gets a number of all decompositions for amass with an error
        allowed. It's similar to thegetDecompositions(double,double) function
        but less space consuming, since doesn't use container to store decompositions
        
        
        :param mass: Mass to be decomposed
        :param error: Error allowed between given and result decomposition
        :return: Number of all decompositions for a given mass and error
        """
        ... 


class SavitzkyGolayFilter:
    """
    Cython implementation of _SavitzkyGolayFilter

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1SavitzkyGolayFilter.html>`_
      -- Inherits from ['DefaultParamHandler', 'ProgressLogger']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void SavitzkyGolayFilter()
        """
        ...
    
    @overload
    def __init__(self, in_0: SavitzkyGolayFilter ) -> None:
        """
        Cython signature: void SavitzkyGolayFilter(SavitzkyGolayFilter &)
        """
        ...
    
    def filter(self, spectrum: MSSpectrum ) -> None:
        """
        Cython signature: void filter(MSSpectrum & spectrum)
        Removed the noise from an MSSpectrum containing profile data
        """
        ...
    
    def filterExperiment(self, exp: MSExperiment ) -> None:
        """
        Cython signature: void filterExperiment(MSExperiment & exp)
        Removed the noise from an MSExperiment containing profile data
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


class SequestOutfile:
    """
    Cython implementation of _SequestOutfile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1SequestOutfile.html>`_

    Representation of a Sequest output file
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void SequestOutfile()
        Representation of a Sequest output file
        """
        ...
    
    @overload
    def __init__(self, in_0: SequestOutfile ) -> None:
        """
        Cython signature: void SequestOutfile(SequestOutfile &)
        """
        ...
    
    def load(self, result_filename: Union[bytes, str, String] , peptide_identifications: List[PeptideIdentification] , protein_identification: ProteinIdentification , p_value_threshold: float , pvalues: List[float] , database: Union[bytes, str, String] , ignore_proteins_per_peptide: bool ) -> None:
        """
        Cython signature: void load(const String & result_filename, libcpp_vector[PeptideIdentification] & peptide_identifications, ProteinIdentification & protein_identification, double p_value_threshold, libcpp_vector[double] & pvalues, const String & database, bool ignore_proteins_per_peptide)
        Loads data from a Sequest outfile
        
        :param result_filename: The file to be loaded
        :param peptide_identifications: The identifications
        :param protein_identification: The protein identifications
        :param p_value_threshold: The significance level (for the peptide hit scores)
        :param pvalues: A list with the pvalues of the peptides (pvalues computed with peptide prophet)
        :param database: The database used for the search
        :param ignore_proteins_per_peptide: This is a hack to deal with files that use a suffix like "+1" in column "Reference", but do not actually list extra protein references in subsequent lines
        """
        ...
    
    def getColumns(self, line: Union[bytes, str, String] , substrings: List[bytes] , number_of_columns: int , reference_column: int ) -> bool:
        """
        Cython signature: bool getColumns(const String & line, libcpp_vector[String] & substrings, size_t number_of_columns, size_t reference_column)
        Retrieves columns from a Sequest outfile line
        """
        ...
    
    def getACAndACType(self, line: Union[bytes, str, String] , accession: String , accession_type: String ) -> None:
        """
        Cython signature: void getACAndACType(String line, String & accession, String & accession_type)
        Retrieves the accession type and accession number from a protein description line
        """
        ...
    
    def __richcmp__(self, other: SequestOutfile, op: int) -> Any:
        ... 


class SignalToNoiseEstimatorMedian:
    """
    Cython implementation of _SignalToNoiseEstimatorMedian[_MSSpectrum]

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1SignalToNoiseEstimatorMedian[_MSSpectrum].html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void SignalToNoiseEstimatorMedian()
        """
        ...
    
    @overload
    def __init__(self, in_0: SignalToNoiseEstimatorMedian ) -> None:
        """
        Cython signature: void SignalToNoiseEstimatorMedian(SignalToNoiseEstimatorMedian &)
        """
        ...
    
    def init(self, spectrum: MSSpectrum ) -> None:
        """
        Cython signature: void init(MSSpectrum & spectrum)
        """
        ...
    
    def getSignalToNoise(self, index: int ) -> float:
        """
        Cython signature: double getSignalToNoise(size_t index)
        """
        ...
    
    def getSparseWindowPercent(self) -> float:
        """
        Cython signature: double getSparseWindowPercent()
        """
        ...
    
    def getHistogramRightmostPercent(self) -> float:
        """
        Cython signature: double getHistogramRightmostPercent()
        """
        ...
    IntensityThresholdCalculation : __IntensityThresholdCalculation 


class SiriusFragmentAnnotation:
    """
    Cython implementation of _SiriusFragmentAnnotation

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1SiriusFragmentAnnotation.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void SiriusFragmentAnnotation()
        """
        ...
    
    @overload
    def __init__(self, in_0: SiriusFragmentAnnotation ) -> None:
        """
        Cython signature: void SiriusFragmentAnnotation(SiriusFragmentAnnotation &)
        """
        ...
    
    def extractAnnotationsFromSiriusFile(self, path_to_sirius_workspace: String , max_rank: int , decoy: bool , use_exact_mass: bool ) -> List[MSSpectrum]:
        """
        Cython signature: libcpp_vector[MSSpectrum] extractAnnotationsFromSiriusFile(String & path_to_sirius_workspace, size_t max_rank, bool decoy, bool use_exact_mass)
        """
        ...
    
    def extractSiriusAnnotationsTgtOnly(self, sirius_workspace_subdirs: List[bytes] , score_threshold: float , use_exact_mass: bool , resolve: bool ) -> List[MSSpectrum]:
        """
        Cython signature: libcpp_vector[MSSpectrum] extractSiriusAnnotationsTgtOnly(libcpp_vector[String] & sirius_workspace_subdirs, double score_threshold, bool use_exact_mass, bool resolve)
        """
        ...
    
    def extractAndResolveSiriusAnnotations(self, sirius_workspace_subdirs: List[bytes] , score_threshold: float , use_exact_mass: bool ) -> List[SiriusFragmentAnnotation_SiriusTargetDecoySpectra]:
        """
        Cython signature: libcpp_vector[SiriusFragmentAnnotation_SiriusTargetDecoySpectra] extractAndResolveSiriusAnnotations(libcpp_vector[String] & sirius_workspace_subdirs, double score_threshold, bool use_exact_mass)
        """
        ... 


class SiriusFragmentAnnotation_SiriusTargetDecoySpectra:
    """
    Cython implementation of _SiriusFragmentAnnotation_SiriusTargetDecoySpectra

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1SiriusFragmentAnnotation_SiriusTargetDecoySpectra.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void SiriusFragmentAnnotation_SiriusTargetDecoySpectra()
        """
        ...
    
    @overload
    def __init__(self, in_0: SiriusFragmentAnnotation_SiriusTargetDecoySpectra ) -> None:
        """
        Cython signature: void SiriusFragmentAnnotation_SiriusTargetDecoySpectra(SiriusFragmentAnnotation_SiriusTargetDecoySpectra &)
        """
        ... 


class SpectrumAccessTransforming:
    """
    Cython implementation of _SpectrumAccessTransforming

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumAccessTransforming.html>`_
      -- Inherits from ['ISpectrumAccess']
    """
    
    def getSpectrumById(self, id_: int ) -> OSSpectrum:
        """
        Cython signature: shared_ptr[OSSpectrum] getSpectrumById(int id_)
        Returns a pointer to a spectrum at the given string id
        """
        ...
    
    def getSpectraByRT(self, RT: float , deltaRT: float ) -> List[int]:
        """
        Cython signature: libcpp_vector[size_t] getSpectraByRT(double RT, double deltaRT)
        Returns a vector of ids of spectra that are within RT +/- deltaRT
        """
        ...
    
    def getNrSpectra(self) -> int:
        """
        Cython signature: size_t getNrSpectra()
        Returns the number of spectra available
        """
        ...
    
    def getChromatogramById(self, id_: int ) -> OSChromatogram:
        """
        Cython signature: shared_ptr[OSChromatogram] getChromatogramById(int id_)
        Returns a pointer to a chromatogram at the given id
        """
        ...
    
    def getNrChromatograms(self) -> int:
        """
        Cython signature: size_t getNrChromatograms()
        Returns the number of chromatograms available
        """
        ...
    
    def getChromatogramNativeID(self, id_: int ) -> str:
        """
        Cython signature: libcpp_utf8_output_string getChromatogramNativeID(int id_)
        """
        ... 


class SpectrumAnnotator:
    """
    Cython implementation of _SpectrumAnnotator

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumAnnotator.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void SpectrumAnnotator()
        Annotates spectra from identifications and theoretical spectra or
        identifications from spectra and theoretical spectra matching
        with various options
        """
        ...
    
    @overload
    def __init__(self, in_0: SpectrumAnnotator ) -> None:
        """
        Cython signature: void SpectrumAnnotator(SpectrumAnnotator &)
        """
        ...
    
    def annotateMatches(self, spec: MSSpectrum , ph: PeptideHit , tg: TheoreticalSpectrumGenerator , sa: SpectrumAlignment ) -> None:
        """
        Cython signature: void annotateMatches(MSSpectrum & spec, PeptideHit & ph, TheoreticalSpectrumGenerator & tg, SpectrumAlignment & sa)
        Adds ion match annotation to the `spec` input spectrum
        
        :param spec: A PeakSpectrum containing the peaks from which the `pi` identifications are made
        :param ph: A spectrum identifications to be used for the annotation, looking up matches from a spectrum and the theoretical spectrum inferred from the identifications sequence
        :param tg: A TheoreticalSpectrumGenerator to infer the theoretical spectrum. Its own parameters define which ion types are referred
        :param sa: A SpectrumAlignment to match the theoretical spectrum with the measured. Its own parameters define the match tolerance
        """
        ...
    
    def addIonMatchStatistics(self, pi: PeptideIdentification , spec: MSSpectrum , tg: TheoreticalSpectrumGenerator , sa: SpectrumAlignment ) -> None:
        """
        Cython signature: void addIonMatchStatistics(PeptideIdentification & pi, MSSpectrum & spec, TheoreticalSpectrumGenerator & tg, SpectrumAlignment & sa)
        Adds ion match statistics to `pi` PeptideIdentifcation
        
        :param pi: A spectrum identifications to be annotated, looking up matches from a spectrum and the theoretical spectrum inferred from the identifications sequence
        :param spec: A PeakSpectrum containing the peaks from which the `pi` identifications are made
        :param tg: A TheoreticalSpectrumGenerator to infer the theoretical spectrum. Its own parameters define which ion types are referred
        :param sa: A SpectrumAlignment to match the theoretical spectrum with the measured. Its own parameters define the match tolerance
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


class SpectrumIdentification:
    """
    Cython implementation of _SpectrumIdentification

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumIdentification.html>`_
      -- Inherits from ['MetaInfoInterface']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void SpectrumIdentification()
        """
        ...
    
    @overload
    def __init__(self, in_0: SpectrumIdentification ) -> None:
        """
        Cython signature: void SpectrumIdentification(SpectrumIdentification &)
        """
        ...
    
    def setHits(self, hits: List[IdentificationHit] ) -> None:
        """
        Cython signature: void setHits(libcpp_vector[IdentificationHit] & hits)
        Sets the identification hits of this spectrum identification (corresponds to single peptide hit in the list)
        """
        ...
    
    def addHit(self, hit: IdentificationHit ) -> None:
        """
        Cython signature: void addHit(IdentificationHit & hit)
        Adds a single identification hit to the hits
        """
        ...
    
    def getHits(self) -> List[IdentificationHit]:
        """
        Cython signature: libcpp_vector[IdentificationHit] getHits()
        Returns the identification hits of this spectrum identification
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
    
    def __richcmp__(self, other: SpectrumIdentification, op: int) -> Any:
        ... 


class SqrtMower:
    """
    Cython implementation of _SqrtMower

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1SqrtMower.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void SqrtMower()
        """
        ...
    
    @overload
    def __init__(self, in_0: SqrtMower ) -> None:
        """
        Cython signature: void SqrtMower(SqrtMower &)
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


class StablePairFinder:
    """
    Cython implementation of _StablePairFinder

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1StablePairFinder.html>`_
      -- Inherits from ['BaseGroupFinder']
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void StablePairFinder()
        """
        ...
    
    def run(self, input_maps: List[ConsensusMap] , result_map: ConsensusMap ) -> None:
        """
        Cython signature: void run(libcpp_vector[ConsensusMap] & input_maps, ConsensusMap & result_map)
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
        Register all derived classes here
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


class SwathFile:
    """
    Cython implementation of _SwathFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1SwathFile.html>`_
      -- Inherits from ['ProgressLogger']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void SwathFile()
        """
        ...
    
    @overload
    def __init__(self, in_0: SwathFile ) -> None:
        """
        Cython signature: void SwathFile(SwathFile &)
        """
        ...
    
    def loadSplit(self, file_list: List[bytes] , tmp: Union[bytes, str, String] , exp_meta: ExperimentalSettings , readoptions: Union[bytes, str, String] ) -> List[SwathMap]:
        """
        Cython signature: libcpp_vector[SwathMap] loadSplit(StringList file_list, String tmp, shared_ptr[ExperimentalSettings] exp_meta, String readoptions)
        Loads a Swath run from a list of split mzML files
        """
        ...
    
    def loadMzML(self, file_: Union[bytes, str, String] , tmp: Union[bytes, str, String] , exp_meta: ExperimentalSettings , readoptions: Union[bytes, str, String] ) -> List[SwathMap]:
        """
        Cython signature: libcpp_vector[SwathMap] loadMzML(String file_, String tmp, shared_ptr[ExperimentalSettings] exp_meta, String readoptions)
        Loads a Swath run from a single mzML file
        
        Using the `plugin_consumer`, you can provide a custom consumer which will be chained
        into the process of loading the data and making it available (depending on `readoptions`).
        This is useful if you want to modify the data a priori or extract some other information using
        MSDataTransformingConsumer (for example). Make sure it leaves the data intact, such that the
        returned SwathMaps are actually useful
        
        :param file: Input filename
        :param tmp: Temporary directory (for cached data)
        :param exp_meta: Experimental metadata from mzML file
        :param readoptions: How are spectra accessed after reading - tradeoff between memory usage and time (disk caching)
        :param plugin_consumer: An intermediate custom consumer
        :returns: Swath maps for MS2 and MS1 (unless readoptions == split, which returns no data)
        """
        ...
    
    def loadMzXML(self, file_: Union[bytes, str, String] , tmp: Union[bytes, str, String] , exp_meta: ExperimentalSettings , readoptions: Union[bytes, str, String] ) -> List[SwathMap]:
        """
        Cython signature: libcpp_vector[SwathMap] loadMzXML(String file_, String tmp, shared_ptr[ExperimentalSettings] exp_meta, String readoptions)
        Loads a Swath run from a single mzXML file
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


class TMTElevenPlexQuantitationMethod:
    """
    Cython implementation of _TMTElevenPlexQuantitationMethod

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1TMTElevenPlexQuantitationMethod.html>`_
      -- Inherits from ['IsobaricQuantitationMethod']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void TMTElevenPlexQuantitationMethod()
        """
        ...
    
    @overload
    def __init__(self, in_0: TMTElevenPlexQuantitationMethod ) -> None:
        """
        Cython signature: void TMTElevenPlexQuantitationMethod(TMTElevenPlexQuantitationMethod &)
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


class TMTSixteenPlexQuantitationMethod:
    """
    Cython implementation of _TMTSixteenPlexQuantitationMethod

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1TMTSixteenPlexQuantitationMethod.html>`_
      -- Inherits from ['IsobaricQuantitationMethod']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void TMTSixteenPlexQuantitationMethod()
        """
        ...
    
    @overload
    def __init__(self, in_0: TMTSixteenPlexQuantitationMethod ) -> None:
        """
        Cython signature: void TMTSixteenPlexQuantitationMethod(TMTSixteenPlexQuantitationMethod &)
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


class TraMLFile:
    """
    Cython implementation of _TraMLFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1TraMLFile.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void TraMLFile()
        """
        ...
    
    @overload
    def __init__(self, in_0: TraMLFile ) -> None:
        """
        Cython signature: void TraMLFile(TraMLFile &)
        """
        ...
    
    def load(self, filename: Union[bytes, str, String] , id: TargetedExperiment ) -> None:
        """
        Cython signature: void load(String filename, TargetedExperiment & id)
        Loads a map from a TraML file
        """
        ...
    
    def store(self, filename: Union[bytes, str, String] , id: TargetedExperiment ) -> None:
        """
        Cython signature: void store(String filename, TargetedExperiment & id)
        Stores a map in a TraML file
        """
        ...
    
    def isSemanticallyValid(self, filename: Union[bytes, str, String] , errors: List[bytes] , warnings: List[bytes] ) -> bool:
        """
        Cython signature: bool isSemanticallyValid(String filename, StringList & errors, StringList & warnings)
        Checks if a file is valid with respect to the mapping file and the controlled vocabulary
        
        :param filename: File name of the file to be checked
        :param errors: Errors during the validation are returned in this output parameter
        :param warnings: Warnings during the validation are returned in this output parameter
        """
        ... 


class TransformationModelBSpline:
    """
    Cython implementation of _TransformationModelBSpline

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1TransformationModelBSpline.html>`_
      -- Inherits from ['TransformationModel']
    """
    
    def __init__(self, data: List[TM_DataPoint] , params: Param ) -> None:
        """
        Cython signature: void TransformationModelBSpline(libcpp_vector[TM_DataPoint] & data, Param & params)
        """
        ...
    
    def getDefaultParameters(self, in_0: Param ) -> None:
        """
        Cython signature: void getDefaultParameters(Param &)
        Gets the default parameters
        """
        ...
    
    def evaluate(self, value: float ) -> float:
        """
        Cython signature: double evaluate(double value)
        Evaluates the model at the given values
        """
        ...
    
    def getParameters(self) -> Param:
        """
        Cython signature: Param getParameters()
        """
        ...
    
    def weightData(self, data: List[TM_DataPoint] ) -> None:
        """
        Cython signature: void weightData(libcpp_vector[TM_DataPoint] & data)
        Weight the data by the given weight function
        """
        ...
    
    def checkValidWeight(self, weight: Union[bytes, str, String] , valid_weights: List[bytes] ) -> bool:
        """
        Cython signature: bool checkValidWeight(const String & weight, libcpp_vector[String] & valid_weights)
        Check for a valid weighting function string
        """
        ...
    
    def weightDatum(self, datum: float , weight: Union[bytes, str, String] ) -> float:
        """
        Cython signature: double weightDatum(double & datum, const String & weight)
        Weight the data according to the weighting function
        """
        ...
    
    def unWeightDatum(self, datum: float , weight: Union[bytes, str, String] ) -> float:
        """
        Cython signature: double unWeightDatum(double & datum, const String & weight)
        Apply the reverse of the weighting function to the data
        """
        ...
    
    def getValidXWeights(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getValidXWeights()
        Returns a list of valid x weight function stringss
        """
        ...
    
    def getValidYWeights(self) -> List[bytes]:
        """
        Cython signature: libcpp_vector[String] getValidYWeights()
        Returns a list of valid y weight function strings
        """
        ...
    
    def unWeightData(self, data: List[TM_DataPoint] ) -> None:
        """
        Cython signature: void unWeightData(libcpp_vector[TM_DataPoint] & data)
        Unweight the data by the given weight function
        """
        ...
    
    def checkDatumRange(self, datum: float , datum_min: float , datum_max: float ) -> float:
        """
        Cython signature: double checkDatumRange(const double & datum, const double & datum_min, const double & datum_max)
        Check that the datum is within the valid min and max bounds
        """
        ...
    
    getDefaultParameters: __static_TransformationModelBSpline_getDefaultParameters 


class UniqueIdGenerator:
    """
    Cython implementation of _UniqueIdGenerator

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1UniqueIdGenerator.html>`_
    """
    
    def getUniqueId(self) -> int:
        """
        Cython signature: uint64_t getUniqueId()
        """
        ...
    
    def setSeed(self, in_0: int ) -> None:
        """
        Cython signature: void setSeed(uint64_t)
        """
        ...
    
    def getSeed(self) -> int:
        """
        Cython signature: uint64_t getSeed()
        """
        ... 


class __IntensityThresholdCalculation:
    None
    MANUAL : int
    AUTOMAXBYSTDEV : int
    AUTOMAXBYPERCENT : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class LogType:
    None
    CMD : int
    GUI : int
    NONE : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class MT_QUANTMETHOD:
    None
    MT_QUANT_AREA : int
    MT_QUANT_MEDIAN : int
    SIZE_OF_MT_QUANTMETHOD : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __PeptideIndexing_ExitCodes:
    None
    EXECUTION_OK : int
    DATABASE_EMPTY : int
    PEPTIDE_IDS_EMPTY : int
    ILLEGAL_PARAMETERS : int
    UNEXPECTED_RESULT : int
    DECOYSTRING_EMPTY : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __PeptidePosition:
    None
    INTERNAL : int
    C_TERM : int
    N_TERM : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __ProteinProteinCrossLinkType:
    None
    CROSS : int
    MONO : int
    LOOP : int
    NUMBER_OF_CROSS_LINK_TYPES : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __QUANT_TYPES:
    None
    MS1LABEL : int
    MS2LABEL : int
    LABELFREE : int
    SIZE_OF_QUANT_TYPES : int

    def getMapping(self) -> Dict[int, str]:
       ... 

