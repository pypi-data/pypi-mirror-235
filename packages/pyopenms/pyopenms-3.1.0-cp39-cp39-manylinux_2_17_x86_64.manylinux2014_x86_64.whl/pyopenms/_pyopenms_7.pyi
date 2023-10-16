from __future__ import annotations
from typing import overload, Any, List, Dict, Tuple, Set, Sequence, Union
from pyopenms import *  # pylint: disable=wildcard-import; lgtm(py/polluting-import)
import numpy as _np

from enum import Enum as _PyEnum


def __static_TransformationModelLinear_getDefaultParameters(in_0: Param ) -> None:
    """
    Cython signature: void getDefaultParameters(Param &)
    """
    ...

def __static_DateTime_now() -> DateTime:
    """
    Cython signature: DateTime now()
    """
    ...


class AASeqWithMass:
    """
    Cython implementation of _AASeqWithMass

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1AASeqWithMass.html>`_
    """
    
    peptide_mass: float
    
    peptide_seq: AASequence
    
    position: int
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void AASeqWithMass()
        """
        ...
    
    @overload
    def __init__(self, in_0: AASeqWithMass ) -> None:
        """
        Cython signature: void AASeqWithMass(AASeqWithMass &)
        """
        ... 


class AMSE_AdductInfo:
    """
    Cython implementation of _AMSE_AdductInfo

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1AMSE_AdductInfo.html>`_
    """
    
    def __init__(self, name: Union[bytes, str, String] , adduct: EmpiricalFormula , charge: int , mol_multiplier: int ) -> None:
        """
        Cython signature: void AMSE_AdductInfo(const String & name, EmpiricalFormula & adduct, int charge, unsigned int mol_multiplier)
        """
        ...
    
    def getNeutralMass(self, observed_mz: float ) -> float:
        """
        Cython signature: double getNeutralMass(double observed_mz)
        """
        ...
    
    def getMZ(self, neutral_mass: float ) -> float:
        """
        Cython signature: double getMZ(double neutral_mass)
        """
        ...
    
    def isCompatible(self, db_entry: EmpiricalFormula ) -> bool:
        """
        Cython signature: bool isCompatible(EmpiricalFormula db_entry)
        """
        ...
    
    def getCharge(self) -> int:
        """
        Cython signature: int getCharge()
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
        """
        ... 


class Adduct:
    """
    Cython implementation of _Adduct

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1Adduct.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void Adduct()
        """
        ...
    
    @overload
    def __init__(self, in_0: Adduct ) -> None:
        """
        Cython signature: void Adduct(Adduct &)
        """
        ...
    
    @overload
    def __init__(self, charge: int ) -> None:
        """
        Cython signature: void Adduct(int charge)
        """
        ...
    
    @overload
    def __init__(self, charge: int , amount: int , singleMass: float , formula: Union[bytes, str, String] , log_prob: float , rt_shift: float , label: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void Adduct(int charge, int amount, double singleMass, String formula, double log_prob, double rt_shift, String label)
        """
        ...
    
    def getCharge(self) -> int:
        """
        Cython signature: int getCharge()
        """
        ...
    
    def setCharge(self, charge: int ) -> None:
        """
        Cython signature: void setCharge(int charge)
        """
        ...
    
    def getAmount(self) -> int:
        """
        Cython signature: int getAmount()
        """
        ...
    
    def setAmount(self, amount: int ) -> None:
        """
        Cython signature: void setAmount(int amount)
        """
        ...
    
    def getSingleMass(self) -> float:
        """
        Cython signature: double getSingleMass()
        """
        ...
    
    def setSingleMass(self, singleMass: float ) -> None:
        """
        Cython signature: void setSingleMass(double singleMass)
        """
        ...
    
    def getLogProb(self) -> float:
        """
        Cython signature: double getLogProb()
        """
        ...
    
    def setLogProb(self, log_prob: float ) -> None:
        """
        Cython signature: void setLogProb(double log_prob)
        """
        ...
    
    def getFormula(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getFormula()
        """
        ...
    
    def setFormula(self, formula: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setFormula(String formula)
        """
        ...
    
    def getRTShift(self) -> float:
        """
        Cython signature: double getRTShift()
        """
        ...
    
    def getLabel(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getLabel()
        """
        ... 


class BaseFeature:
    """
    Cython implementation of _BaseFeature

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1BaseFeature.html>`_
      -- Inherits from ['UniqueIdInterface', 'RichPeak2D']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void BaseFeature()
        """
        ...
    
    @overload
    def __init__(self, in_0: BaseFeature ) -> None:
        """
        Cython signature: void BaseFeature(BaseFeature &)
        """
        ...
    
    def getQuality(self) -> float:
        """
        Cython signature: float getQuality()
        Returns the overall quality
        """
        ...
    
    def setQuality(self, q: float ) -> None:
        """
        Cython signature: void setQuality(float q)
        Sets the overall quality
        """
        ...
    
    def getWidth(self) -> float:
        """
        Cython signature: float getWidth()
        Returns the features width (full width at half max, FWHM)
        """
        ...
    
    def setWidth(self, q: float ) -> None:
        """
        Cython signature: void setWidth(float q)
        Sets the width of the feature (FWHM)
        """
        ...
    
    def getCharge(self) -> int:
        """
        Cython signature: int getCharge()
        Returns the charge state
        """
        ...
    
    def setCharge(self, q: int ) -> None:
        """
        Cython signature: void setCharge(int q)
        Sets the charge state
        """
        ...
    
    def getAnnotationState(self) -> int:
        """
        Cython signature: AnnotationState getAnnotationState()
        State of peptide identifications attached to this feature. If one ID has multiple hits, the output depends on the top-hit only
        """
        ...
    
    def getPeptideIdentifications(self) -> List[PeptideIdentification]:
        """
        Cython signature: libcpp_vector[PeptideIdentification] getPeptideIdentifications()
        Returns the PeptideIdentification vector
        """
        ...
    
    def setPeptideIdentifications(self, peptides: List[PeptideIdentification] ) -> None:
        """
        Cython signature: void setPeptideIdentifications(libcpp_vector[PeptideIdentification] & peptides)
        Sets the PeptideIdentification vector
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
    
    def __richcmp__(self, other: BaseFeature, op: int) -> Any:
        ... 


class BilinearInterpolation:
    """
    Cython implementation of _BilinearInterpolation[double,double]

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::Math_1_1BilinearInterpolation[double,double].html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void BilinearInterpolation()
        """
        ...
    
    @overload
    def __init__(self, in_0: BilinearInterpolation ) -> None:
        """
        Cython signature: void BilinearInterpolation(BilinearInterpolation &)
        """
        ...
    
    def value(self, arg_pos_0: float , arg_pos_1: float ) -> float:
        """
        Cython signature: double value(double arg_pos_0, double arg_pos_1)
        """
        ...
    
    def addValue(self, arg_pos_0: float , arg_pos_1: float , arg_value: float ) -> None:
        """
        Cython signature: void addValue(double arg_pos_0, double arg_pos_1, double arg_value)
        Performs bilinear resampling. The arg_value is split up and added to the data points around arg_pos. ("forward resampling")
        """
        ...
    
    def getData(self) -> MatrixDouble:
        """
        Cython signature: MatrixDouble getData()
        """
        ...
    
    def setData(self, data: MatrixDouble ) -> None:
        """
        Cython signature: void setData(MatrixDouble & data)
        Assigns data to the internal random access container storing the data. SourceContainer must be assignable to ContainerType
        """
        ...
    
    def empty(self) -> bool:
        """
        Cython signature: bool empty()
        """
        ...
    
    def key2index_0(self, pos: float ) -> float:
        """
        Cython signature: double key2index_0(double pos)
        The transformation from "outside" to "inside" coordinates
        """
        ...
    
    def index2key_0(self, pos: float ) -> float:
        """
        Cython signature: double index2key_0(double pos)
        The transformation from "inside" to "outside" coordinates
        """
        ...
    
    def key2index_1(self, pos: float ) -> float:
        """
        Cython signature: double key2index_1(double pos)
        The transformation from "outside" to "inside" coordinates
        """
        ...
    
    def index2key_1(self, pos: float ) -> float:
        """
        Cython signature: double index2key_1(double pos)
        The transformation from "inside" to "outside" coordinates
        """
        ...
    
    def getScale_0(self) -> float:
        """
        Cython signature: double getScale_0()
        """
        ...
    
    def setScale_0(self, scale: float ) -> None:
        """
        Cython signature: void setScale_0(double & scale)
        """
        ...
    
    def getScale_1(self) -> float:
        """
        Cython signature: double getScale_1()
        """
        ...
    
    def setScale_1(self, scale: float ) -> None:
        """
        Cython signature: void setScale_1(double & scale)
        """
        ...
    
    def getOffset_0(self) -> float:
        """
        Cython signature: double getOffset_0()
        Accessor. "Offset" is the point (in "outside" units) which corresponds to "Data(0,0)"
        """
        ...
    
    def setOffset_0(self, offset: float ) -> None:
        """
        Cython signature: void setOffset_0(double & offset)
        """
        ...
    
    def getOffset_1(self) -> float:
        """
        Cython signature: double getOffset_1()
        Accessor. "Offset" is the point (in "outside" units) which corresponds to "Data(0,0)"
        """
        ...
    
    def setOffset_1(self, offset: float ) -> None:
        """
        Cython signature: void setOffset_1(double & offset)
        """
        ...
    
    @overload
    def setMapping_0(self, scale: float , inside: float , outside: float ) -> None:
        """
        Cython signature: void setMapping_0(double & scale, double & inside, double & outside)
        """
        ...
    
    @overload
    def setMapping_0(self, inside_low: float , outside_low: float , inside_high: float , outside_high: float ) -> None:
        """
        Cython signature: void setMapping_0(double & inside_low, double & outside_low, double & inside_high, double & outside_high)
        """
        ...
    
    @overload
    def setMapping_1(self, scale: float , inside: float , outside: float ) -> None:
        """
        Cython signature: void setMapping_1(double & scale, double & inside, double & outside)
        """
        ...
    
    @overload
    def setMapping_1(self, inside_low: float , outside_low: float , inside_high: float , outside_high: float ) -> None:
        """
        Cython signature: void setMapping_1(double & inside_low, double & outside_low, double & inside_high, double & outside_high)
        """
        ...
    
    def getInsideReferencePoint_0(self) -> float:
        """
        Cython signature: double getInsideReferencePoint_0()
        """
        ...
    
    def getInsideReferencePoint_1(self) -> float:
        """
        Cython signature: double getInsideReferencePoint_1()
        """
        ...
    
    def getOutsideReferencePoint_0(self) -> float:
        """
        Cython signature: double getOutsideReferencePoint_0()
        """
        ...
    
    def getOutsideReferencePoint_1(self) -> float:
        """
        Cython signature: double getOutsideReferencePoint_1()
        """
        ...
    
    def supportMin_0(self) -> float:
        """
        Cython signature: double supportMin_0()
        Lower boundary of the support, in "outside" coordinates
        """
        ...
    
    def supportMin_1(self) -> float:
        """
        Cython signature: double supportMin_1()
        Lower boundary of the support, in "outside" coordinates
        """
        ...
    
    def supportMax_0(self) -> float:
        """
        Cython signature: double supportMax_0()
        Upper boundary of the support, in "outside" coordinates
        """
        ...
    
    def supportMax_1(self) -> float:
        """
        Cython signature: double supportMax_1()
        Upper boundary of the support, in "outside" coordinates
        """
        ... 


class ChargePair:
    """
    Cython implementation of _ChargePair

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ChargePair.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ChargePair()
        """
        ...
    
    @overload
    def __init__(self, in_0: ChargePair ) -> None:
        """
        Cython signature: void ChargePair(ChargePair &)
        """
        ...
    
    @overload
    def __init__(self, index0: int , index1: int , charge0: int , charge1: int , compomer: Compomer , mass_diff: float , active: bool ) -> None:
        """
        Cython signature: void ChargePair(size_t index0, size_t index1, int charge0, int charge1, Compomer compomer, double mass_diff, bool active)
        """
        ...
    
    def getCharge(self, pairID: int ) -> int:
        """
        Cython signature: int getCharge(unsigned int pairID)
        Returns the charge (for element 0 or 1)
        """
        ...
    
    def setCharge(self, pairID: int , e: int ) -> None:
        """
        Cython signature: void setCharge(unsigned int pairID, int e)
        Sets the charge (for element 0 or 1)
        """
        ...
    
    def getElementIndex(self, pairID: int ) -> int:
        """
        Cython signature: size_t getElementIndex(unsigned int pairID)
        Returns the element index (for element 0 or 1)
        """
        ...
    
    def setElementIndex(self, pairID: int , e: int ) -> None:
        """
        Cython signature: void setElementIndex(unsigned int pairID, size_t e)
        Sets the element index (for element 0 or 1)
        """
        ...
    
    def getCompomer(self) -> Compomer:
        """
        Cython signature: Compomer getCompomer()
        Returns the Id of the compomer that explains the mass difference
        """
        ...
    
    def setCompomer(self, compomer: Compomer ) -> None:
        """
        Cython signature: void setCompomer(Compomer & compomer)
        Sets the compomer id
        """
        ...
    
    def getMassDiff(self) -> float:
        """
        Cython signature: double getMassDiff()
        Returns the mass difference
        """
        ...
    
    def setMassDiff(self, mass_diff: float ) -> None:
        """
        Cython signature: void setMassDiff(double mass_diff)
        Sets the mass difference
        """
        ...
    
    def getEdgeScore(self) -> float:
        """
        Cython signature: double getEdgeScore()
        Returns the ILP edge score
        """
        ...
    
    def setEdgeScore(self, score: float ) -> None:
        """
        Cython signature: void setEdgeScore(double score)
        Sets the ILP edge score
        """
        ...
    
    def isActive(self) -> bool:
        """
        Cython signature: bool isActive()
        Is this pair realized?
        """
        ...
    
    def setActive(self, active: bool ) -> None:
        """
        Cython signature: void setActive(bool active)
        """
        ... 


class ChromatogramTools:
    """
    Cython implementation of _ChromatogramTools

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ChromatogramTools.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ChromatogramTools()
        """
        ...
    
    @overload
    def __init__(self, in_0: ChromatogramTools ) -> None:
        """
        Cython signature: void ChromatogramTools(ChromatogramTools &)
        """
        ...
    
    def convertChromatogramsToSpectra(self, epx: MSExperiment ) -> None:
        """
        Cython signature: void convertChromatogramsToSpectra(MSExperiment & epx)
        Converts the chromatogram to a list of spectra with instrument settings
        """
        ...
    
    def convertSpectraToChromatograms(self, epx: MSExperiment , remove_spectra: bool , force_conversion: bool ) -> None:
        """
        Cython signature: void convertSpectraToChromatograms(MSExperiment & epx, bool remove_spectra, bool force_conversion)
        Converts e.g. SRM spectra to chromatograms
        """
        ... 


class ComplementFilter:
    """
    Cython implementation of _ComplementFilter

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ComplementFilter.html>`_
      -- Inherits from ['FilterFunctor']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ComplementFilter()
        Total intensity of peak pairs that could result from complementing fragments of charge state 1
        """
        ...
    
    @overload
    def __init__(self, in_0: ComplementFilter ) -> None:
        """
        Cython signature: void ComplementFilter(ComplementFilter &)
        """
        ...
    
    def apply(self, in_0: MSSpectrum ) -> float:
        """
        Cython signature: double apply(MSSpectrum &)
        Returns the total intensity of peak pairs which could result from complementing fragments
        """
        ...
    
    def getProductName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getProductName()
        Returns the name for registration at the factory
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


class ComplementMarker:
    """
    Cython implementation of _ComplementMarker

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ComplementMarker.html>`_
      -- Inherits from ['PeakMarker']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ComplementMarker()
        ComplementMarker marks peak pairs which could represent y - b ion pairs
        """
        ...
    
    @overload
    def __init__(self, in_0: ComplementMarker ) -> None:
        """
        Cython signature: void ComplementMarker(ComplementMarker &)
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


class ConsensusIDAlgorithmBest:
    """
    Cython implementation of _ConsensusIDAlgorithmBest

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ConsensusIDAlgorithmBest.html>`_
      -- Inherits from ['ConsensusIDAlgorithmIdentity']
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void ConsensusIDAlgorithmBest()
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


class ConsensusIDAlgorithmSimilarity:
    """
    Cython implementation of _ConsensusIDAlgorithmSimilarity

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ConsensusIDAlgorithmSimilarity.html>`_
      -- Inherits from ['ConsensusIDAlgorithm']
    """
    
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


class ConsensusMapNormalizerAlgorithmMedian:
    """
    Cython implementation of _ConsensusMapNormalizerAlgorithmMedian

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::ConsensusMapNormalizerAlgorithmMedian_1_1ConsensusMapNormalizerAlgorithmMedian.html>`_
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void ConsensusMapNormalizerAlgorithmMedian()
        """
        ...
    
    def computeMedians(self, input_map: ConsensusMap , medians: List[float] , acc_filter: Union[bytes, str, String] , desc_filter: Union[bytes, str, String] ) -> int:
        """
        Cython signature: size_t computeMedians(ConsensusMap & input_map, libcpp_vector[double] & medians, const String & acc_filter, const String & desc_filter)
        Computes medians of all maps and returns index of map with most features
        """
        ...
    
    def normalizeMaps(self, input_map: ConsensusMap , method: int , acc_filter: Union[bytes, str, String] , desc_filter: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void normalizeMaps(ConsensusMap & input_map, NormalizationMethod method, const String & acc_filter, const String & desc_filter)
        Normalizes the maps of the consensusMap
        """
        ... 


class ContinuousWaveletTransform:
    """
    Cython implementation of _ContinuousWaveletTransform

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ContinuousWaveletTransform.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ContinuousWaveletTransform()
        """
        ...
    
    @overload
    def __init__(self, in_0: ContinuousWaveletTransform ) -> None:
        """
        Cython signature: void ContinuousWaveletTransform(ContinuousWaveletTransform &)
        """
        ...
    
    def getSignal(self) -> List[Peak1D]:
        """
        Cython signature: libcpp_vector[Peak1D] getSignal()
        Returns the wavelet transform of the signal
        """
        ...
    
    def setSignal(self, signal: List[Peak1D] ) -> None:
        """
        Cython signature: void setSignal(libcpp_vector[Peak1D] & signal)
        Sets the wavelet transform of the signal
        """
        ...
    
    def getWavelet(self) -> List[float]:
        """
        Cython signature: libcpp_vector[double] getWavelet()
        Returns the wavelet
        """
        ...
    
    def setWavelet(self, wavelet: List[float] ) -> None:
        """
        Cython signature: void setWavelet(libcpp_vector[double] & wavelet)
        Sets the signal
        """
        ...
    
    def getScale(self) -> float:
        """
        Cython signature: double getScale()
        Returns the scale of the wavelet
        """
        ...
    
    def setScale(self, scale: float ) -> None:
        """
        Cython signature: void setScale(double scale)
        Sets the spacing of raw data
        """
        ...
    
    def getSpacing(self) -> float:
        """
        Cython signature: double getSpacing()
        Returns the spacing of raw data
        """
        ...
    
    def setSpacing(self, spacing: float ) -> None:
        """
        Cython signature: void setSpacing(double spacing)
        Sets the spacing of raw data
        """
        ...
    
    def getLeftPaddingIndex(self) -> int:
        """
        Cython signature: ptrdiff_t getLeftPaddingIndex()
        Returns the position where the signal starts (in the interval [0,end_left_padding_) are the padded zeros)
        """
        ...
    
    def setLeftPaddingIndex(self, end_left_padding: int ) -> None:
        """
        Cython signature: void setLeftPaddingIndex(ptrdiff_t end_left_padding)
        Sets the position where the signal starts
        """
        ...
    
    def getRightPaddingIndex(self) -> int:
        """
        Cython signature: ptrdiff_t getRightPaddingIndex()
        Returns the position where the signal ends (in the interval (begin_right_padding_,end] are the padded zeros)
        """
        ...
    
    def setRightPaddingIndex(self, begin_right_padding: int ) -> None:
        """
        Cython signature: void setRightPaddingIndex(ptrdiff_t begin_right_padding)
        Sets the position where the signal starts
        """
        ...
    
    def getSignalLength(self) -> int:
        """
        Cython signature: ptrdiff_t getSignalLength()
        Returns the signal length [end_left_padding,begin_right_padding]
        """
        ...
    
    def setSignalLength(self, signal_length: int ) -> None:
        """
        Cython signature: void setSignalLength(ptrdiff_t signal_length)
        Sets the signal length [end_left_padding,begin_right_padding]
        """
        ...
    
    def getSize(self) -> int:
        """
        Cython signature: int getSize()
        Returns the signal length including padded zeros [0,end]
        """
        ...
    
    def init(self, scale: float , spacing: float ) -> None:
        """
        Cython signature: void init(double scale, double spacing)
        Perform possibly necessary preprocessing steps, like tabulating the Wavelet
        """
        ... 


class ContinuousWaveletTransformNumIntegration:
    """
    Cython implementation of _ContinuousWaveletTransformNumIntegration

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ContinuousWaveletTransformNumIntegration.html>`_
      -- Inherits from ['ContinuousWaveletTransform']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ContinuousWaveletTransformNumIntegration()
        """
        ...
    
    @overload
    def __init__(self, in_0: ContinuousWaveletTransformNumIntegration ) -> None:
        """
        Cython signature: void ContinuousWaveletTransformNumIntegration(ContinuousWaveletTransformNumIntegration &)
        """
        ...
    
    def getSignal(self) -> List[Peak1D]:
        """
        Cython signature: libcpp_vector[Peak1D] getSignal()
        Returns the wavelet transform of the signal
        """
        ...
    
    def setSignal(self, signal: List[Peak1D] ) -> None:
        """
        Cython signature: void setSignal(libcpp_vector[Peak1D] & signal)
        Sets the wavelet transform of the signal
        """
        ...
    
    def getWavelet(self) -> List[float]:
        """
        Cython signature: libcpp_vector[double] getWavelet()
        Returns the wavelet
        """
        ...
    
    def setWavelet(self, wavelet: List[float] ) -> None:
        """
        Cython signature: void setWavelet(libcpp_vector[double] & wavelet)
        Sets the signal
        """
        ...
    
    def getScale(self) -> float:
        """
        Cython signature: double getScale()
        Returns the scale of the wavelet
        """
        ...
    
    def setScale(self, scale: float ) -> None:
        """
        Cython signature: void setScale(double scale)
        Sets the spacing of raw data
        """
        ...
    
    def getSpacing(self) -> float:
        """
        Cython signature: double getSpacing()
        Returns the spacing of raw data
        """
        ...
    
    def setSpacing(self, spacing: float ) -> None:
        """
        Cython signature: void setSpacing(double spacing)
        Sets the spacing of raw data
        """
        ...
    
    def getLeftPaddingIndex(self) -> int:
        """
        Cython signature: ptrdiff_t getLeftPaddingIndex()
        Returns the position where the signal starts (in the interval [0,end_left_padding_) are the padded zeros)
        """
        ...
    
    def setLeftPaddingIndex(self, end_left_padding: int ) -> None:
        """
        Cython signature: void setLeftPaddingIndex(ptrdiff_t end_left_padding)
        Sets the position where the signal starts
        """
        ...
    
    def getRightPaddingIndex(self) -> int:
        """
        Cython signature: ptrdiff_t getRightPaddingIndex()
        Returns the position where the signal ends (in the interval (begin_right_padding_,end] are the padded zeros)
        """
        ...
    
    def setRightPaddingIndex(self, begin_right_padding: int ) -> None:
        """
        Cython signature: void setRightPaddingIndex(ptrdiff_t begin_right_padding)
        Sets the position where the signal starts
        """
        ...
    
    def getSignalLength(self) -> int:
        """
        Cython signature: ptrdiff_t getSignalLength()
        Returns the signal length [end_left_padding,begin_right_padding]
        """
        ...
    
    def setSignalLength(self, signal_length: int ) -> None:
        """
        Cython signature: void setSignalLength(ptrdiff_t signal_length)
        Sets the signal length [end_left_padding,begin_right_padding]
        """
        ...
    
    def getSize(self) -> int:
        """
        Cython signature: int getSize()
        Returns the signal length including padded zeros [0,end]
        """
        ...
    
    def init(self, scale: float , spacing: float ) -> None:
        """
        Cython signature: void init(double scale, double spacing)
        Perform possibly necessary preprocessing steps, like tabulating the Wavelet
        """
        ... 


class CrossLinkSpectrumMatch:
    """
    Cython implementation of _CrossLinkSpectrumMatch

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::OPXLDataStructs_1_1CrossLinkSpectrumMatch.html>`_
    """
    
    cross_link: ProteinProteinCrossLink
    
    scan_index_light: int
    
    scan_index_heavy: int
    
    score: float
    
    rank: int
    
    xquest_score: float
    
    pre_score: float
    
    percTIC: float
    
    wTIC: float
    
    wTICold: float
    
    int_sum: float
    
    intsum_alpha: float
    
    intsum_beta: float
    
    total_current: float
    
    precursor_error_ppm: float
    
    match_odds: float
    
    match_odds_alpha: float
    
    match_odds_beta: float
    
    log_occupancy: float
    
    log_occupancy_alpha: float
    
    log_occupancy_beta: float
    
    xcorrx_max: float
    
    xcorrc_max: float
    
    matched_linear_alpha: int
    
    matched_linear_beta: int
    
    matched_xlink_alpha: int
    
    matched_xlink_beta: int
    
    num_iso_peaks_mean: float
    
    num_iso_peaks_mean_linear_alpha: float
    
    num_iso_peaks_mean_linear_beta: float
    
    num_iso_peaks_mean_xlinks_alpha: float
    
    num_iso_peaks_mean_xlinks_beta: float
    
    ppm_error_abs_sum_linear_alpha: float
    
    ppm_error_abs_sum_linear_beta: float
    
    ppm_error_abs_sum_xlinks_alpha: float
    
    ppm_error_abs_sum_xlinks_beta: float
    
    ppm_error_abs_sum_linear: float
    
    ppm_error_abs_sum_xlinks: float
    
    ppm_error_abs_sum_alpha: float
    
    ppm_error_abs_sum_beta: float
    
    ppm_error_abs_sum: float
    
    precursor_correction: int
    
    precursor_total_intensity: float
    
    precursor_target_intensity: float
    
    precursor_signal_proportion: float
    
    precursor_target_peak_count: int
    
    precursor_residual_peak_count: int
    
    frag_annotations: List[PeptideHit_PeakAnnotation]
    
    peptide_id_index: int
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void CrossLinkSpectrumMatch()
        """
        ...
    
    @overload
    def __init__(self, in_0: CrossLinkSpectrumMatch ) -> None:
        """
        Cython signature: void CrossLinkSpectrumMatch(CrossLinkSpectrumMatch &)
        """
        ... 


class DBoundingBox2:
    """
    Cython implementation of _DBoundingBox2

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1DBoundingBox2.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void DBoundingBox2()
        """
        ...
    
    @overload
    def __init__(self, in_0: DBoundingBox2 ) -> None:
        """
        Cython signature: void DBoundingBox2(DBoundingBox2 &)
        """
        ...
    
    def minPosition(self) -> Union[Sequence[int], Sequence[float]]:
        """
        Cython signature: DPosition2 minPosition()
        """
        ...
    
    def maxPosition(self) -> Union[Sequence[int], Sequence[float]]:
        """
        Cython signature: DPosition2 maxPosition()
        """
        ... 


class DateTime:
    """
    Cython implementation of _DateTime

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1DateTime.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void DateTime()
        """
        ...
    
    @overload
    def __init__(self, in_0: DateTime ) -> None:
        """
        Cython signature: void DateTime(DateTime &)
        """
        ...
    
    def setDate(self, date: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setDate(String date)
        """
        ...
    
    def setTime(self, date: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setTime(String date)
        """
        ...
    
    def getDate(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getDate()
        """
        ...
    
    def getTime(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getTime()
        """
        ...
    
    def now(self) -> DateTime:
        """
        Cython signature: DateTime now()
        """
        ...
    
    def clear(self) -> None:
        """
        Cython signature: void clear()
        """
        ...
    
    def get(self) -> Union[bytes, str, String]:
        """
        Cython signature: String get()
        """
        ...
    
    def set(self, date: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void set(String date)
        """
        ...
    
    now: __static_DateTime_now 


class DecoyGenerator:
    """
    Cython implementation of _DecoyGenerator

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1DecoyGenerator.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void DecoyGenerator()
        """
        ...
    
    @overload
    def __init__(self, in_0: DecoyGenerator ) -> None:
        """
        Cython signature: void DecoyGenerator(DecoyGenerator &)
        """
        ...
    
    def setSeed(self, in_0: int ) -> None:
        """
        Cython signature: void setSeed(uint64_t)
        """
        ...
    
    def reverseProtein(self, protein: AASequence ) -> AASequence:
        """
        Cython signature: AASequence reverseProtein(const AASequence & protein)
        Reverses the protein sequence
        """
        ...
    
    def reversePeptides(self, protein: AASequence , protease: Union[bytes, str, String] ) -> AASequence:
        """
        Cython signature: AASequence reversePeptides(const AASequence & protein, const String & protease)
        Reverses the protein's peptide sequences between enzymatic cutting positions
        """
        ...
    
    def shufflePeptides(self, aas: AASequence , protease: Union[bytes, str, String] , max_attempts: int ) -> AASequence:
        """
        Cython signature: AASequence shufflePeptides(const AASequence & aas, const String & protease, const int max_attempts)
        Shuffle the protein's peptide sequences between enzymatic cutting positions, each peptide is shuffled @param max_attempts times to minimize sequence identity
        """
        ... 


class EDTAFile:
    """
    Cython implementation of _EDTAFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1EDTAFile.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void EDTAFile()
        """
        ...
    
    @overload
    def __init__(self, in_0: EDTAFile ) -> None:
        """
        Cython signature: void EDTAFile(EDTAFile &)
        """
        ...
    
    @overload
    def store(self, filename: Union[bytes, str, String] , map: FeatureMap ) -> None:
        """
        Cython signature: void store(String filename, FeatureMap & map)
        """
        ...
    
    @overload
    def store(self, filename: Union[bytes, str, String] , map: ConsensusMap ) -> None:
        """
        Cython signature: void store(String filename, ConsensusMap & map)
        """
        ...
    
    def load(self, filename: Union[bytes, str, String] , consensus_map: ConsensusMap ) -> None:
        """
        Cython signature: void load(String filename, ConsensusMap & consensus_map)
        """
        ... 


class EmgFitter1D:
    """
    Cython implementation of _EmgFitter1D

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1EmgFitter1D.html>`_
      -- Inherits from ['LevMarqFitter1D']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void EmgFitter1D()
        Exponentially modified gaussian distribution fitter (1-dim.) using Levenberg-Marquardt algorithm (Eigen implementation) for parameter optimization
        """
        ...
    
    @overload
    def __init__(self, in_0: EmgFitter1D ) -> None:
        """
        Cython signature: void EmgFitter1D(EmgFitter1D &)
        """
        ...
    
    def getProductName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getProductName()
        Name of the model (needed by Factory)
        """
        ... 


class FeatureFinderAlgorithmMetaboIdent:
    """
    Cython implementation of _FeatureFinderAlgorithmMetaboIdent

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureFinderAlgorithmMetaboIdent.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void FeatureFinderAlgorithmMetaboIdent()
        """
        ...
    
    def setMSData(self, input: MSExperiment ) -> None:
        """
        Cython signature: void setMSData(MSExperiment & input)
        Sets spectra
        """
        ...
    
    def getMSData(self) -> MSExperiment:
        """
        Cython signature: const MSExperiment & getMSData()
        Returns spectra
        """
        ...
    
    def run(self, metaboIdentTable: List[FeatureFinderMetaboIdentCompound] , features: FeatureMap , spectra_path: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void run(const libcpp_vector[FeatureFinderMetaboIdentCompound] metaboIdentTable, FeatureMap & features, String spectra_path)
         Run feature extraction. spectra_path get's annotated as primaryMSRunPath in the resulting feature map.
        """
        ...
    
    def getChromatograms(self) -> MSExperiment:
        """
        Cython signature: MSExperiment & getChromatograms()
        Retrieves chromatograms (empty if run was not executed)
        """
        ...
    
    def getLibrary(self) -> TargetedExperiment:
        """
        Cython signature: const TargetedExperiment & getLibrary()
        Retrieves the assay library (e.g., to store as TraML, empty if run was not executed)
        """
        ...
    
    def getTransformations(self) -> TransformationDescription:
        """
        Cython signature: const TransformationDescription & getTransformations()
        Retrieves deviations between provided coordinates and extacted ones (e.g., to store as TrafoXML or for plotting)
        """
        ...
    
    def getNShared(self) -> int:
        """
        Cython signature: size_t getNShared()
        Retrieves number of features with shared identifications
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


class FeatureFinderMetaboIdentCompound:
    """
    Cython implementation of _FeatureFinderMetaboIdentCompound

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureFinderMetaboIdentCompound.html>`_
    """
    
    def __init__(self, name: Union[bytes, str, String] , formula: Union[bytes, str, String] , mass: float , charges: List[int] , rts: List[float] , rt_ranges: List[float] , iso_distrib: List[float] ) -> None:
        """
        Cython signature: void FeatureFinderMetaboIdentCompound(String name, String formula, double mass, libcpp_vector[int] charges, libcpp_vector[double] rts, libcpp_vector[double] rt_ranges, libcpp_vector[double] iso_distrib)
          Represents a compound in the in the FeatureFinderMetaboIdent library table.
        
        
          :param name: Unique name for the target compound.
          :param formula: Chemical sum formula.
          :param mass: Neutral mass; if zero calculated from formula.
          :param charges: List of possible charge states.
          :param rts: List of possible retention times.
          :param rt_ranges: List of possible retention time ranges (window around RT), either one value or one per RT entry.
          :param iso_distrib: List of relative abundances of isotopologues; if zero calculated from formula.
        """
        ...
    
    def getName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getName()
          Gets the compound name.
        
        
          :rtype: str
        """
        ...
    
    def getFormula(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getFormula()
          Gets the compound chemical formula.
        
        
          :rtype: str
        """
        ...
    
    def getMass(self) -> float:
        """
        Cython signature: double getMass()
          Gets the compound mass.
        
        
          :rtype: float
        """
        ...
    
    def getCharges(self) -> List[int]:
        """
        Cython signature: libcpp_vector[int] getCharges()
          Gets the compound charge states.
        
        
          :rtype: list of int
        """
        ...
    
    def getRTs(self) -> List[float]:
        """
        Cython signature: libcpp_vector[double] getRTs()
          Gets the compound retention times.
        
        
          :rtype: list of float
        """
        ...
    
    def getRTRanges(self) -> List[float]:
        """
        Cython signature: libcpp_vector[double] getRTRanges()
          Gets the compound retention time ranges.
        
        
          :rtype: list of float
        """
        ...
    
    def getIsotopeDistribution(self) -> List[float]:
        """
        Cython signature: libcpp_vector[double] getIsotopeDistribution()
          Gets the compound isotopic distributions.
        
        
          :rtype: list of float
        """
        ... 


class FeatureGroupingAlgorithmKD:
    """
    Cython implementation of _FeatureGroupingAlgorithmKD

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureGroupingAlgorithmKD.html>`_
      -- Inherits from ['FeatureGroupingAlgorithm', 'ProgressLogger']
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void FeatureGroupingAlgorithmKD()
        A feature grouping algorithm for unlabeled data
        """
        ...
    
    @overload
    def group(self, maps: List[FeatureMap] , out: ConsensusMap ) -> None:
        """
        Cython signature: void group(libcpp_vector[FeatureMap] & maps, ConsensusMap & out)
        """
        ...
    
    @overload
    def group(self, maps: List[ConsensusMap] , out: ConsensusMap ) -> None:
        """
        Cython signature: void group(libcpp_vector[ConsensusMap] & maps, ConsensusMap & out)
        """
        ...
    
    def getProductName(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getProductName()
        Returns the product name (for the Factory)
        """
        ...
    
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


class GaussTraceFitter:
    """
    Cython implementation of _GaussTraceFitter

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1GaussTraceFitter.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void GaussTraceFitter()
        Fitter for RT profiles using a Gaussian background model
        """
        ...
    
    @overload
    def __init__(self, in_0: GaussTraceFitter ) -> None:
        """
        Cython signature: void GaussTraceFitter(GaussTraceFitter &)
        """
        ...
    
    def fit(self, traces: MassTraces ) -> None:
        """
        Cython signature: void fit(MassTraces & traces)
        Override important methods
        """
        ...
    
    def getLowerRTBound(self) -> float:
        """
        Cython signature: double getLowerRTBound()
        Returns the lower RT bound
        """
        ...
    
    def getUpperRTBound(self) -> float:
        """
        Cython signature: double getUpperRTBound()
        Returns the upper RT bound
        """
        ...
    
    def getHeight(self) -> float:
        """
        Cython signature: double getHeight()
        Returns height of the fitted gaussian model
        """
        ...
    
    def getCenter(self) -> float:
        """
        Cython signature: double getCenter()
        Returns center of the fitted gaussian model
        """
        ...
    
    def getFWHM(self) -> float:
        """
        Cython signature: double getFWHM()
        Returns FWHM of the fitted gaussian model
        """
        ...
    
    def getSigma(self) -> float:
        """
        Cython signature: double getSigma()
        Returns Sigma of the fitted gaussian model
        """
        ...
    
    def checkMaximalRTSpan(self, max_rt_span: float ) -> bool:
        """
        Cython signature: bool checkMaximalRTSpan(double max_rt_span)
        """
        ...
    
    def checkMinimalRTSpan(self, rt_bounds: List[float, float] , min_rt_span: float ) -> bool:
        """
        Cython signature: bool checkMinimalRTSpan(libcpp_pair[double,double] & rt_bounds, double min_rt_span)
        """
        ...
    
    def computeTheoretical(self, trace: MassTrace , k: int ) -> float:
        """
        Cython signature: double computeTheoretical(MassTrace & trace, size_t k)
        """
        ...
    
    def getArea(self) -> float:
        """
        Cython signature: double getArea()
        Returns area of the fitted gaussian model
        """
        ...
    
    def getGnuplotFormula(self, trace: MassTrace , function_name: bytes , baseline: float , rt_shift: float ) -> Union[bytes, str, String]:
        """
        Cython signature: String getGnuplotFormula(MassTrace & trace, char function_name, double baseline, double rt_shift)
        """
        ...
    
    def getValue(self, rt: float ) -> float:
        """
        Cython signature: double getValue(double rt)
        Returns value of the fitted gaussian model
        """
        ... 


class ILPDCWrapper:
    """
    Cython implementation of _ILPDCWrapper

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ILPDCWrapper.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ILPDCWrapper()
        """
        ...
    
    @overload
    def __init__(self, in_0: ILPDCWrapper ) -> None:
        """
        Cython signature: void ILPDCWrapper(ILPDCWrapper &)
        """
        ...
    
    def compute(self, fm: FeatureMap , pairs: List[ChargePair] , verbose_level: int ) -> float:
        """
        Cython signature: double compute(FeatureMap fm, libcpp_vector[ChargePair] & pairs, size_t verbose_level)
        Compute optimal solution and return value of objective function. If the input feature map is empty, a warning is issued and -1 is returned
        """
        ... 


class IdXMLFile:
    """
    Cython implementation of _IdXMLFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1IdXMLFile.html>`_
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void IdXMLFile()
        Used to load and store idXML files
        """
        ...
    
    def load(self, filename: Union[bytes, str, String] , protein_ids: List[ProteinIdentification] , peptide_ids: List[PeptideIdentification] ) -> None:
        """
        Cython signature: void load(String filename, libcpp_vector[ProteinIdentification] & protein_ids, libcpp_vector[PeptideIdentification] & peptide_ids)
        Loads the identifications of an idXML file without identifier
        """
        ...
    
    @overload
    def store(self, filename: Union[bytes, str, String] , protein_ids: List[ProteinIdentification] , peptide_ids: List[PeptideIdentification] , document_id: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void store(String filename, libcpp_vector[ProteinIdentification] & protein_ids, libcpp_vector[PeptideIdentification] & peptide_ids, String document_id)
        Stores the data in an idXML file
        """
        ...
    
    @overload
    def store(self, filename: Union[bytes, str, String] , protein_ids: List[ProteinIdentification] , peptide_ids: List[PeptideIdentification] ) -> None:
        """
        Cython signature: void store(String filename, libcpp_vector[ProteinIdentification] & protein_ids, libcpp_vector[PeptideIdentification] & peptide_ids)
        """
        ... 


class IonSource:
    """
    Cython implementation of _IonSource

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1IonSource.html>`_
      -- Inherits from ['MetaInfoInterface']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void IonSource()
        Description of an ion source (part of a MS Instrument)
        """
        ...
    
    @overload
    def __init__(self, in_0: IonSource ) -> None:
        """
        Cython signature: void IonSource(IonSource &)
        """
        ...
    
    def getPolarity(self) -> int:
        """
        Cython signature: Polarity getPolarity()
        Returns the ionization mode
        """
        ...
    
    def setPolarity(self, polarity: int ) -> None:
        """
        Cython signature: void setPolarity(Polarity polarity)
        Sets the ionization mode
        """
        ...
    
    def getInletType(self) -> int:
        """
        Cython signature: InletType getInletType()
        Returns the inlet type
        """
        ...
    
    def setInletType(self, inlet_type: int ) -> None:
        """
        Cython signature: void setInletType(InletType inlet_type)
        Sets the inlet type
        """
        ...
    
    def getIonizationMethod(self) -> int:
        """
        Cython signature: IonizationMethod getIonizationMethod()
        Returns the ionization method
        """
        ...
    
    def setIonizationMethod(self, ionization_type: int ) -> None:
        """
        Cython signature: void setIonizationMethod(IonizationMethod ionization_type)
        Sets the ionization method
        """
        ...
    
    def getOrder(self) -> int:
        """
        Cython signature: int getOrder()
        Returns the position of this part in the whole Instrument
        
        Order can be ignored, as long the instrument has this default setup:
          - one ion source
          - one or many mass analyzers
          - one ion detector
        
        For more complex instruments, the order should be defined.
        """
        ...
    
    def setOrder(self, order: int ) -> None:
        """
        Cython signature: void setOrder(int order)
        Sets the order
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
    
    def __richcmp__(self, other: IonSource, op: int) -> Any:
        ...
    InletType : __InletType
    IonizationMethod : __IonizationMethod
    Polarity : __Polarity 


class IsotopeWavelet:
    """
    Cython implementation of _IsotopeWavelet

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1IsotopeWavelet.html>`_
    """
    
    def destroy(self) -> None:
        """
        Cython signature: void destroy()
        Deletes the singleton instance
        """
        ...
    
    def getValueByMass(self, t: float , m: float , z: int , mode: int ) -> float:
        """
        Cython signature: double getValueByMass(double t, double m, unsigned int z, int mode)
        Returns the value of the isotope wavelet at position `t`. Usually, you do not need to call this function\n
        
        Note that this functions returns the pure function value of psi and not the normalized (average=0)
        value given by Psi
        
        
        :param t: The position at which the wavelet has to be drawn (within the coordinate system of the wavelet)
        :param m: The m/z position within the signal (i.e. the mass not de-charged) within the signal
        :param z: The charge `z` we want to detect
        :param mode: Indicates whether positive mode (+1) or negative mode (-1) has been used for ionization
        """
        ...
    
    def getValueByLambda(self, lambda_: float , tz1: float ) -> float:
        """
        Cython signature: double getValueByLambda(double lambda_, double tz1)
        Returns the value of the isotope wavelet at position `t` via a fast table lookup\n
        
        Usually, you do not need to call this function
        Please use `sampleTheWavelet` instead
        Note that this functions returns the pure function value of psi and not the normalized (average=0)
        value given by Psi
        
        
        :param lambda: The mass-parameter lambda
        :param tz1: t (the position) times the charge (z) plus 1
        """
        ...
    
    def getValueByLambdaExtrapol(self, lambda_: float , tz1: float ) -> float:
        """
        Cython signature: double getValueByLambdaExtrapol(double lambda_, double tz1)
        Returns the value of the isotope wavelet at position `t`\n
        
        This function is usually significantly slower than the table lookup performed in @see getValueByLambda
        Nevertheless, it might be necessary to call this function due to extrapolating reasons caused by the
        alignment of the wavelet\n
        
        Usually, you do not need to call this function
        Please use `sampleTheWavelet` instead
        Note that this functions returns the pure function value of psi and not the normalized (average=0)
        value given by Psi
        
        
        :param lambda: The mass-parameter lambda
        :param tz1: t (the position) times the charge (z) plus 1
        """
        ...
    
    def getValueByLambdaExact(self, lambda_: float , tz1: float ) -> float:
        """
        Cython signature: double getValueByLambdaExact(double lambda_, double tz1)
        """
        ...
    
    def getMaxCharge(self) -> int:
        """
        Cython signature: unsigned int getMaxCharge()
        Returns the largest charge state we will consider
        """
        ...
    
    def setMaxCharge(self, max_charge: int ) -> None:
        """
        Cython signature: void setMaxCharge(unsigned int max_charge)
        Sets the `max_charge` parameter
        """
        ...
    
    def getTableSteps(self) -> float:
        """
        Cython signature: double getTableSteps()
        Returns the table_steps_ parameter
        """
        ...
    
    def getInvTableSteps(self) -> float:
        """
        Cython signature: double getInvTableSteps()
        Returns the inv_table_steps_ parameter
        """
        ...
    
    def setTableSteps(self, table_steps: float ) -> None:
        """
        Cython signature: void setTableSteps(double table_steps)
        Sets the `table_steps` parameter
        """
        ...
    
    def getLambdaL(self, m: float ) -> float:
        """
        Cython signature: double getLambdaL(double m)
        Returns the mass-parameter lambda (linear fit)
        """
        ...
    
    def getGammaTableMaxIndex(self) -> int:
        """
        Cython signature: size_t getGammaTableMaxIndex()
        Returns the largest possible index for the pre-sampled gamma table
        """
        ...
    
    def getExpTableMaxIndex(self) -> int:
        """
        Cython signature: size_t getExpTableMaxIndex()
        Returns the largest possible index for the pre-sampled exp table
        """
        ...
    
    def myPow(self, a: float , b: float ) -> float:
        """
        Cython signature: float myPow(float a, float b)
        Internally used function; uses register shifts for fast computation of the power function
        """
        ...
    
    def getMzPeakCutOffAtMonoPos(self, mass: float , z: int ) -> int:
        """
        Cython signature: unsigned int getMzPeakCutOffAtMonoPos(double mass, unsigned int z)
        """
        ...
    
    @overload
    def getNumPeakCutOff(self, mass: float , z: int ) -> int:
        """
        Cython signature: unsigned int getNumPeakCutOff(double mass, unsigned int z)
        """
        ...
    
    @overload
    def getNumPeakCutOff(self, mz: float ) -> int:
        """
        Cython signature: unsigned int getNumPeakCutOff(double mz)
        """
        ... 


class LightMRMTransitionGroupCP:
    """
    Cython implementation of _MRMTransitionGroup[_MSChromatogram,_LightTransition]

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMTransitionGroup[_MSChromatogram,_LightTransition].html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void LightMRMTransitionGroupCP()
        """
        ...
    
    @overload
    def __init__(self, in_0: LightMRMTransitionGroupCP ) -> None:
        """
        Cython signature: void LightMRMTransitionGroupCP(LightMRMTransitionGroupCP &)
        """
        ...
    
    def size(self) -> int:
        """
        Cython signature: size_t size()
        """
        ...
    
    def getTransitionGroupID(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getTransitionGroupID()
        """
        ...
    
    def setTransitionGroupID(self, tr_gr_id: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setTransitionGroupID(String tr_gr_id)
        """
        ...
    
    def getTransitions(self) -> List[LightTransition]:
        """
        Cython signature: libcpp_vector[LightTransition] getTransitions()
        """
        ...
    
    def getTransitionsMuteable(self) -> List[LightTransition]:
        """
        Cython signature: libcpp_vector[LightTransition] getTransitionsMuteable()
        """
        ...
    
    def addTransition(self, transition: LightTransition , key: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void addTransition(LightTransition transition, String key)
        """
        ...
    
    def getTransition(self, key: Union[bytes, str, String] ) -> LightTransition:
        """
        Cython signature: LightTransition getTransition(String key)
        """
        ...
    
    def hasTransition(self, key: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool hasTransition(String key)
        """
        ...
    
    def getChromatograms(self) -> List[MSChromatogram]:
        """
        Cython signature: libcpp_vector[MSChromatogram] getChromatograms()
        """
        ...
    
    def addChromatogram(self, chromatogram: MSChromatogram , key: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void addChromatogram(MSChromatogram chromatogram, String key)
        """
        ...
    
    def getChromatogram(self, key: Union[bytes, str, String] ) -> MSChromatogram:
        """
        Cython signature: MSChromatogram getChromatogram(String key)
        """
        ...
    
    def hasChromatogram(self, key: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool hasChromatogram(String key)
        """
        ...
    
    def getPrecursorChromatograms(self) -> List[MSChromatogram]:
        """
        Cython signature: libcpp_vector[MSChromatogram] getPrecursorChromatograms()
        """
        ...
    
    def addPrecursorChromatogram(self, chromatogram: MSChromatogram , key: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void addPrecursorChromatogram(MSChromatogram chromatogram, String key)
        """
        ...
    
    def getPrecursorChromatogram(self, key: Union[bytes, str, String] ) -> MSChromatogram:
        """
        Cython signature: MSChromatogram getPrecursorChromatogram(String key)
        """
        ...
    
    def hasPrecursorChromatogram(self, key: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool hasPrecursorChromatogram(String key)
        """
        ...
    
    def getFeatures(self) -> List[MRMFeature]:
        """
        Cython signature: libcpp_vector[MRMFeature] getFeatures()
        """
        ...
    
    def getFeaturesMuteable(self) -> List[MRMFeature]:
        """
        Cython signature: libcpp_vector[MRMFeature] getFeaturesMuteable()
        """
        ...
    
    def addFeature(self, feature: MRMFeature ) -> None:
        """
        Cython signature: void addFeature(MRMFeature feature)
        """
        ...
    
    def getBestFeature(self) -> MRMFeature:
        """
        Cython signature: MRMFeature getBestFeature()
        """
        ...
    
    def getLibraryIntensity(self, result: List[float] ) -> None:
        """
        Cython signature: void getLibraryIntensity(libcpp_vector[double] result)
        """
        ...
    
    def subset(self, tr_ids: List[Union[bytes, str]] ) -> LightMRMTransitionGroupCP:
        """
        Cython signature: LightMRMTransitionGroupCP subset(libcpp_vector[libcpp_utf8_string] tr_ids)
        """
        ...
    
    def isInternallyConsistent(self) -> bool:
        """
        Cython signature: bool isInternallyConsistent()
        """
        ...
    
    def chromatogramIdsMatch(self) -> bool:
        """
        Cython signature: bool chromatogramIdsMatch()
        """
        ... 


class LinearResampler:
    """
    Cython implementation of _LinearResampler

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1LinearResampler.html>`_
      -- Inherits from ['DefaultParamHandler', 'ProgressLogger']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void LinearResampler()
        """
        ...
    
    @overload
    def __init__(self, in_0: LinearResampler ) -> None:
        """
        Cython signature: void LinearResampler(LinearResampler &)
        """
        ...
    
    def raster(self, input: MSSpectrum ) -> None:
        """
        Cython signature: void raster(MSSpectrum & input)
        Applies the resampling algorithm to an MSSpectrum
        """
        ...
    
    def rasterExperiment(self, input: MSExperiment ) -> None:
        """
        Cython signature: void rasterExperiment(MSExperiment & input)
        Resamples the data in an MSExperiment
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


class MRMFeaturePickerFile:
    """
    Cython implementation of _MRMFeaturePickerFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMFeaturePickerFile.html>`_

    _MRMFeaturePickerFile_ loads components and components groups parameters from a .csv file
    
    The structures defined in [MRMFeaturePicker](@ref MRMFeaturePicker) are used
    
    It is required that columns `component_name` and `component_group_name` are present.
    Lines whose `component_name`'s or `component_group_name`'s value is an empty string, will be skipped.
    The class supports the absence of information within other columns.
    
    A reduced example of the expected format (fewer columns are shown here):
    > component_name,component_group_name,TransitionGroupPicker:stop_after_feature,TransitionGroupPicker:PeakPickerMRM:sgolay_frame_length
    > arg-L.arg-L_1.Heavy,arg-L,2,15
    > arg-L.arg-L_1.Light,arg-L,2,17
    > orn.orn_1.Heavy,orn,3,21
    > orn.orn_1.Light,orn,3,13
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MRMFeaturePickerFile()
        """
        ...
    
    @overload
    def __init__(self, in_0: MRMFeaturePickerFile ) -> None:
        """
        Cython signature: void MRMFeaturePickerFile(MRMFeaturePickerFile &)
        """
        ...
    
    def load(self, filename: Union[bytes, str, String] , cp_list: List[MRMFP_ComponentParams] , cgp_list: List[MRMFP_ComponentGroupParams] ) -> None:
        """
        Cython signature: void load(const String & filename, libcpp_vector[MRMFP_ComponentParams] & cp_list, libcpp_vector[MRMFP_ComponentGroupParams] & cgp_list)
        Loads the file's data and saves it into vectors of `ComponentParams` and `ComponentGroupParams`
        
        The file is expected to contain at least two columns: `component_name` and `component_group_name`. Otherwise,
        an exception is thrown
        
        If a component group (identified by its name) is found multiple times, only the first one is saved
        
        
        :param filename: Path to the .csv input file
        :param cp_list: Component params are saved in this list
        :param cgp_list: Component Group params are saved in this list
        :raises:
          Exception: MissingInformation If the required columns are not found
        :raises:
          Exception: FileNotFound If input file is not found
        """
        ... 


class MRMTransitionGroupCP:
    """
    Cython implementation of _MRMTransitionGroup[_MSChromatogram,_ReactionMonitoringTransition]

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMTransitionGroup[_MSChromatogram,_ReactionMonitoringTransition].html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MRMTransitionGroupCP()
        """
        ...
    
    @overload
    def __init__(self, in_0: MRMTransitionGroupCP ) -> None:
        """
        Cython signature: void MRMTransitionGroupCP(MRMTransitionGroupCP &)
        """
        ...
    
    def size(self) -> int:
        """
        Cython signature: size_t size()
        """
        ...
    
    def getTransitionGroupID(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getTransitionGroupID()
        """
        ...
    
    def setTransitionGroupID(self, tr_gr_id: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setTransitionGroupID(String tr_gr_id)
        """
        ...
    
    def getTransitions(self) -> List[ReactionMonitoringTransition]:
        """
        Cython signature: libcpp_vector[ReactionMonitoringTransition] getTransitions()
        """
        ...
    
    def getTransitionsMuteable(self) -> List[ReactionMonitoringTransition]:
        """
        Cython signature: libcpp_vector[ReactionMonitoringTransition] getTransitionsMuteable()
        """
        ...
    
    def addTransition(self, transition: ReactionMonitoringTransition , key: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void addTransition(ReactionMonitoringTransition transition, String key)
        """
        ...
    
    def getTransition(self, key: Union[bytes, str, String] ) -> ReactionMonitoringTransition:
        """
        Cython signature: ReactionMonitoringTransition getTransition(String key)
        """
        ...
    
    def hasTransition(self, key: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool hasTransition(String key)
        """
        ...
    
    def getChromatograms(self) -> List[MSChromatogram]:
        """
        Cython signature: libcpp_vector[MSChromatogram] getChromatograms()
        """
        ...
    
    def addChromatogram(self, chromatogram: MSChromatogram , key: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void addChromatogram(MSChromatogram chromatogram, String key)
        """
        ...
    
    def getChromatogram(self, key: Union[bytes, str, String] ) -> MSChromatogram:
        """
        Cython signature: MSChromatogram getChromatogram(String key)
        """
        ...
    
    def hasChromatogram(self, key: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool hasChromatogram(String key)
        """
        ...
    
    def getPrecursorChromatograms(self) -> List[MSChromatogram]:
        """
        Cython signature: libcpp_vector[MSChromatogram] getPrecursorChromatograms()
        """
        ...
    
    def addPrecursorChromatogram(self, chromatogram: MSChromatogram , key: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void addPrecursorChromatogram(MSChromatogram chromatogram, String key)
        """
        ...
    
    def getPrecursorChromatogram(self, key: Union[bytes, str, String] ) -> MSChromatogram:
        """
        Cython signature: MSChromatogram getPrecursorChromatogram(String key)
        """
        ...
    
    def hasPrecursorChromatogram(self, key: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool hasPrecursorChromatogram(String key)
        """
        ...
    
    def getFeatures(self) -> List[MRMFeature]:
        """
        Cython signature: libcpp_vector[MRMFeature] getFeatures()
        """
        ...
    
    def getFeaturesMuteable(self) -> List[MRMFeature]:
        """
        Cython signature: libcpp_vector[MRMFeature] getFeaturesMuteable()
        """
        ...
    
    def addFeature(self, feature: MRMFeature ) -> None:
        """
        Cython signature: void addFeature(MRMFeature feature)
        """
        ...
    
    def getBestFeature(self) -> MRMFeature:
        """
        Cython signature: MRMFeature getBestFeature()
        """
        ...
    
    def getLibraryIntensity(self, result: List[float] ) -> None:
        """
        Cython signature: void getLibraryIntensity(libcpp_vector[double] result)
        """
        ...
    
    def subset(self, tr_ids: List[Union[bytes, str]] ) -> MRMTransitionGroupCP:
        """
        Cython signature: MRMTransitionGroupCP subset(libcpp_vector[libcpp_utf8_string] tr_ids)
        """
        ...
    
    def isInternallyConsistent(self) -> bool:
        """
        Cython signature: bool isInternallyConsistent()
        """
        ...
    
    def chromatogramIdsMatch(self) -> bool:
        """
        Cython signature: bool chromatogramIdsMatch()
        """
        ... 


class MRMTransitionGroupPicker:
    """
    Cython implementation of _MRMTransitionGroupPicker

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMTransitionGroupPicker.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MRMTransitionGroupPicker()
        """
        ...
    
    @overload
    def __init__(self, in_0: MRMTransitionGroupPicker ) -> None:
        """
        Cython signature: void MRMTransitionGroupPicker(MRMTransitionGroupPicker &)
        """
        ...
    
    @overload
    def pickTransitionGroup(self, transition_group: LightMRMTransitionGroupCP ) -> None:
        """
        Cython signature: void pickTransitionGroup(LightMRMTransitionGroupCP transition_group)
        """
        ...
    
    @overload
    def pickTransitionGroup(self, transition_group: MRMTransitionGroupCP ) -> None:
        """
        Cython signature: void pickTransitionGroup(MRMTransitionGroupCP transition_group)
        """
        ...
    
    def createMRMFeature(self, transition_group: LightMRMTransitionGroupCP , picked_chroms: List[MSChromatogram] , smoothed_chroms: List[MSChromatogram] , chr_idx: int , peak_idx: int ) -> MRMFeature:
        """
        Cython signature: MRMFeature createMRMFeature(LightMRMTransitionGroupCP transition_group, libcpp_vector[MSChromatogram] & picked_chroms, libcpp_vector[MSChromatogram] & smoothed_chroms, const int chr_idx, const int peak_idx)
        """
        ...
    
    def remove_overlapping_features(self, picked_chroms: List[MSChromatogram] , best_left: float , best_right: float ) -> None:
        """
        Cython signature: void remove_overlapping_features(libcpp_vector[MSChromatogram] & picked_chroms, double best_left, double best_right)
        """
        ...
    
    def findLargestPeak(self, picked_chroms: List[MSChromatogram] , chr_idx: int , peak_idx: int ) -> None:
        """
        Cython signature: void findLargestPeak(libcpp_vector[MSChromatogram] & picked_chroms, int & chr_idx, int & peak_idx)
        """
        ...
    
    def findWidestPeakIndices(self, picked_chroms: List[MSChromatogram] , chrom_idx: int , point_idx: int ) -> None:
        """
        Cython signature: void findWidestPeakIndices(libcpp_vector[MSChromatogram] & picked_chroms, int & chrom_idx, int & point_idx)
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


class MSDataSqlConsumer:
    """
    Cython implementation of _MSDataSqlConsumer

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSDataSqlConsumer.html>`_
    """
    
    @overload
    def __init__(self, filename: Union[bytes, str, String] , run_id: int , buffer_size: int , full_meta: bool , lossy_compression: bool , linear_mass_acc: float ) -> None:
        """
        Cython signature: void MSDataSqlConsumer(String filename, uint64_t run_id, int buffer_size, bool full_meta, bool lossy_compression, double linear_mass_acc)
        """
        ...
    
    @overload
    def __init__(self, in_0: MSDataSqlConsumer ) -> None:
        """
        Cython signature: void MSDataSqlConsumer(MSDataSqlConsumer &)
        """
        ...
    
    def flush(self) -> None:
        """
        Cython signature: void flush()
        Flushes the data for good
        
        After calling this function, no more data is held in the buffer but the
        class is still able to receive new data
        """
        ...
    
    def consumeSpectrum(self, s: MSSpectrum ) -> None:
        """
        Cython signature: void consumeSpectrum(MSSpectrum & s)
        Write a spectrum to the output file
        """
        ...
    
    def consumeChromatogram(self, c: MSChromatogram ) -> None:
        """
        Cython signature: void consumeChromatogram(MSChromatogram & c)
        Write a chromatogram to the output file
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


class MSExperiment:
    """
    Cython implementation of _MSExperiment

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSExperiment.html>`_
      -- Inherits from ['ExperimentalSettings', 'RangeManagerRtMzInt']

    In-Memory representation of a mass spectrometry experiment.
    
    Contains the data and metadata of an experiment performed with an MS (or
    HPLC and MS). This representation of an MS experiment is organized as list
    of spectra and chromatograms and provides an in-memory representation of
    popular mass-spectrometric file formats such as mzXML or mzML. The
    meta-data associated with an experiment is contained in
    ExperimentalSettings (by inheritance) while the raw data (as well as
    spectra and chromatogram level meta data) is stored in objects of type
    MSSpectrum and MSChromatogram, which are accessible through the getSpectrum
    and getChromatogram functions.
    
    Spectra can be accessed by direct iteration or by getSpectrum(),
    while chromatograms are accessed through getChromatogram().
    See help(ExperimentalSettings) for information about meta-data.
    
    Usage:
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MSExperiment()
        """
        ...
    
    @overload
    def __init__(self, in_0: MSExperiment ) -> None:
        """
        Cython signature: void MSExperiment(MSExperiment &)
        """
        ...
    
    def getExperimentalSettings(self) -> ExperimentalSettings:
        """
        Cython signature: ExperimentalSettings getExperimentalSettings()
        """
        ...
    
    def __getitem__(self, in_0: int ) -> MSSpectrum:
        """
        Cython signature: MSSpectrum & operator[](size_t)
        """
        ...
    def __setitem__(self, key: int, value: MSSpectrum ) -> None:
        """Cython signature: MSSpectrum & operator[](size_t)"""
        ...
    
    def addSpectrum(self, spec: MSSpectrum ) -> None:
        """
        Cython signature: void addSpectrum(MSSpectrum spec)
        """
        ...
    
    def setSpectra(self, spectra: List[MSSpectrum] ) -> None:
        """
        Cython signature: void setSpectra(libcpp_vector[MSSpectrum] & spectra)
        """
        ...
    
    def getSpectra(self) -> List[MSSpectrum]:
        """
        Cython signature: libcpp_vector[MSSpectrum] getSpectra()
        """
        ...
    
    def addChromatogram(self, chromatogram: MSChromatogram ) -> None:
        """
        Cython signature: void addChromatogram(MSChromatogram chromatogram)
        """
        ...
    
    def setChromatograms(self, chromatograms: List[MSChromatogram] ) -> None:
        """
        Cython signature: void setChromatograms(libcpp_vector[MSChromatogram] chromatograms)
        """
        ...
    
    def getChromatograms(self) -> List[MSChromatogram]:
        """
        Cython signature: libcpp_vector[MSChromatogram] getChromatograms()
        """
        ...
    
    def calculateTIC(self) -> MSChromatogram:
        """
        Cython signature: MSChromatogram calculateTIC()
        Returns the total ion chromatogram
        """
        ...
    
    def clear(self, clear_meta_data: bool ) -> None:
        """
        Cython signature: void clear(bool clear_meta_data)
        Clear all spectra data and meta data (if called with True)
        """
        ...
    
    @overload
    def updateRanges(self, ) -> None:
        """
        Cython signature: void updateRanges()
        Recalculate global RT and m/z ranges after changes to the data has been made.
        """
        ...
    
    @overload
    def updateRanges(self, msLevel: int ) -> None:
        """
        Cython signature: void updateRanges(int msLevel)
        Recalculate RT and m/z ranges for a specific MS level
        """
        ...
    
    def reserveSpaceSpectra(self, s: int ) -> None:
        """
        Cython signature: void reserveSpaceSpectra(size_t s)
        """
        ...
    
    def reserveSpaceChromatograms(self, s: int ) -> None:
        """
        Cython signature: void reserveSpaceChromatograms(size_t s)
        """
        ...
    
    def getSize(self) -> int:
        """
        Cython signature: uint64_t getSize()
        Returns the total number of peaks
        """
        ...
    
    def size(self) -> int:
        """
        Cython signature: int size()
        """
        ...
    
    def resize(self, s: int ) -> None:
        """
        Cython signature: void resize(size_t s)
        """
        ...
    
    def empty(self) -> bool:
        """
        Cython signature: bool empty()
        """
        ...
    
    def reserve(self, s: int ) -> None:
        """
        Cython signature: void reserve(size_t s)
        """
        ...
    
    def getNrSpectra(self) -> int:
        """
        Cython signature: size_t getNrSpectra()
        Returns the number of MS spectra
        """
        ...
    
    def getNrChromatograms(self) -> int:
        """
        Cython signature: size_t getNrChromatograms()
        Returns the number of chromatograms
        """
        ...
    
    @overload
    def sortSpectra(self, sort_mz: bool ) -> None:
        """
        Cython signature: void sortSpectra(bool sort_mz)
        Sorts spectra by RT. If sort_mz=True also sort each peak in a spectrum by m/z
        """
        ...
    
    @overload
    def sortSpectra(self, ) -> None:
        """
        Cython signature: void sortSpectra()
        """
        ...
    
    @overload
    def sortChromatograms(self, sort_rt: bool ) -> None:
        """
        Cython signature: void sortChromatograms(bool sort_rt)
        Sorts chromatograms by m/z. If sort_rt=True also sort each chromatogram RT
        """
        ...
    
    @overload
    def sortChromatograms(self, ) -> None:
        """
        Cython signature: void sortChromatograms()
        """
        ...
    
    @overload
    def isSorted(self, check_mz: bool ) -> bool:
        """
        Cython signature: bool isSorted(bool check_mz)
        Checks if all spectra are sorted with respect to ascending RT
        """
        ...
    
    @overload
    def isSorted(self, ) -> bool:
        """
        Cython signature: bool isSorted()
        """
        ...
    
    def getPrimaryMSRunPath(self, toFill: List[bytes] ) -> None:
        """
        Cython signature: void getPrimaryMSRunPath(StringList & toFill)
        References to the first MS file(s) after conversions. Used to trace results back to original data.
        """
        ...
    
    def swap(self, in_0: MSExperiment ) -> None:
        """
        Cython signature: void swap(MSExperiment)
        """
        ...
    
    def reset(self) -> None:
        """
        Cython signature: void reset()
        """
        ...
    
    def clearMetaDataArrays(self) -> bool:
        """
        Cython signature: bool clearMetaDataArrays()
        """
        ...
    
    def getPrecursorSpectrum(self, zero_based_index: int ) -> int:
        """
        Cython signature: int getPrecursorSpectrum(int zero_based_index)
        Returns the index of the precursor spectrum for spectrum at index @p zero_based_index
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
    
    def getMinRT(self) -> float:
        """
        Cython signature: double getMinRT()
        Returns the minimum RT
        """
        ...
    
    def getMaxRT(self) -> float:
        """
        Cython signature: double getMaxRT()
        Returns the maximum RT
        """
        ...
    
    def getMinMZ(self) -> float:
        """
        Cython signature: double getMinMZ()
        Returns the minimum m/z
        """
        ...
    
    def getMaxMZ(self) -> float:
        """
        Cython signature: double getMaxMZ()
        Returns the maximum m/z
        """
        ...
    
    def getMinIntensity(self) -> float:
        """
        Cython signature: double getMinIntensity()
        Returns the minimum intensity
        """
        ...
    
    def getMaxIntensity(self) -> float:
        """
        Cython signature: double getMaxIntensity()
        Returns the maximum intensity
        """
        ...
    
    def clearRanges(self) -> None:
        """
        Cython signature: void clearRanges()
        Resets all range dimensions as empty
        """
        ...
    
    def __richcmp__(self, other: MSExperiment, op: int) -> Any:
        ...
    
    def __iter__(self) -> MSSpectrum:
       ... 


class MapConversion:
    """
    Cython implementation of _MapConversion

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MapConversion.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MapConversion()
        """
        ...
    
    @overload
    def __init__(self, in_0: MapConversion ) -> None:
        """
        Cython signature: void MapConversion(MapConversion &)
        """
        ...
    
    @overload
    def convert(self, input_map_index: int , input_map: FeatureMap , output_map: ConsensusMap , n: int ) -> None:
        """
        Cython signature: void convert(uint64_t input_map_index, FeatureMap input_map, ConsensusMap & output_map, size_t n)
        """
        ...
    
    @overload
    def convert(self, input_map_index: int , input_map: MSExperiment , output_map: ConsensusMap , n: int ) -> None:
        """
        Cython signature: void convert(uint64_t input_map_index, MSExperiment & input_map, ConsensusMap & output_map, size_t n)
        """
        ...
    
    @overload
    def convert(self, input_map: ConsensusMap , keep_uids: bool , output_map: FeatureMap ) -> None:
        """
        Cython signature: void convert(ConsensusMap input_map, bool keep_uids, FeatureMap & output_map)
        """
        ... 


class MassAnalyzer:
    """
    Cython implementation of _MassAnalyzer

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MassAnalyzer.html>`_
      -- Inherits from ['MetaInfoInterface']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MassAnalyzer()
        """
        ...
    
    @overload
    def __init__(self, in_0: MassAnalyzer ) -> None:
        """
        Cython signature: void MassAnalyzer(MassAnalyzer &)
        """
        ...
    
    def getType(self) -> int:
        """
        Cython signature: AnalyzerType getType()
        Returns the analyzer type
        """
        ...
    
    def setType(self, type: int ) -> None:
        """
        Cython signature: void setType(AnalyzerType type)
        Sets the analyzer type
        """
        ...
    
    def getResolutionMethod(self) -> int:
        """
        Cython signature: ResolutionMethod getResolutionMethod()
        Returns the method used for determination of the resolution
        """
        ...
    
    def setResolutionMethod(self, resolution_method: int ) -> None:
        """
        Cython signature: void setResolutionMethod(ResolutionMethod resolution_method)
        Sets the method used for determination of the resolution
        """
        ...
    
    def getResolutionType(self) -> int:
        """
        Cython signature: ResolutionType getResolutionType()
        Returns the resolution type
        """
        ...
    
    def setResolutionType(self, resolution_type: int ) -> None:
        """
        Cython signature: void setResolutionType(ResolutionType resolution_type)
        Sets the resolution type
        """
        ...
    
    def getScanDirection(self) -> int:
        """
        Cython signature: ScanDirection getScanDirection()
        Returns the direction of scanning
        """
        ...
    
    def setScanDirection(self, scan_direction: int ) -> None:
        """
        Cython signature: void setScanDirection(ScanDirection scan_direction)
        Sets the direction of scanning
        """
        ...
    
    def getScanLaw(self) -> int:
        """
        Cython signature: ScanLaw getScanLaw()
        Returns the scan law
        """
        ...
    
    def setScanLaw(self, scan_law: int ) -> None:
        """
        Cython signature: void setScanLaw(ScanLaw scan_law)
        Sets the scan law
        """
        ...
    
    def getReflectronState(self) -> int:
        """
        Cython signature: ReflectronState getReflectronState()
        Returns the reflectron state (for TOF)
        """
        ...
    
    def setReflectronState(self, reflecton_state: int ) -> None:
        """
        Cython signature: void setReflectronState(ReflectronState reflecton_state)
        Sets the reflectron state (for TOF)
        """
        ...
    
    def getResolution(self) -> float:
        """
        Cython signature: double getResolution()
        Returns the resolution. The maximum m/z value at which two peaks can be resolved, according to one of the standard measures
        """
        ...
    
    def setResolution(self, resolution: float ) -> None:
        """
        Cython signature: void setResolution(double resolution)
        Sets the resolution
        """
        ...
    
    def getAccuracy(self) -> float:
        """
        Cython signature: double getAccuracy()
        Returns the mass accuracy i.e. how much the theoretical mass may differ from the measured mass (in ppm)
        """
        ...
    
    def setAccuracy(self, accuracy: float ) -> None:
        """
        Cython signature: void setAccuracy(double accuracy)
        Sets the accuracy i.e. how much the theoretical mass may differ from the measured mass (in ppm)
        """
        ...
    
    def getScanRate(self) -> float:
        """
        Cython signature: double getScanRate()
        Returns the scan rate (in s)
        """
        ...
    
    def setScanRate(self, scan_rate: float ) -> None:
        """
        Cython signature: void setScanRate(double scan_rate)
        Sets the scan rate (in s)
        """
        ...
    
    def getScanTime(self) -> float:
        """
        Cython signature: double getScanTime()
        Returns the scan time for a single scan (in s)
        """
        ...
    
    def setScanTime(self, scan_time: float ) -> None:
        """
        Cython signature: void setScanTime(double scan_time)
        Sets the scan time for a single scan (in s)
        """
        ...
    
    def getTOFTotalPathLength(self) -> float:
        """
        Cython signature: double getTOFTotalPathLength()
        Returns the path length for a TOF mass analyzer (in meter)
        """
        ...
    
    def setTOFTotalPathLength(self, TOF_total_path_length: float ) -> None:
        """
        Cython signature: void setTOFTotalPathLength(double TOF_total_path_length)
        Sets the path length for a TOF mass analyzer (in meter)
        """
        ...
    
    def getIsolationWidth(self) -> float:
        """
        Cython signature: double getIsolationWidth()
        Returns the isolation width i.e. in which m/z range the precursor ion is selected for MS to the n (in m/z)
        """
        ...
    
    def setIsolationWidth(self, isolation_width: float ) -> None:
        """
        Cython signature: void setIsolationWidth(double isolation_width)
        Sets the isolation width i.e. in which m/z range the precursor ion is selected for MS to the n (in m/z)
        """
        ...
    
    def getFinalMSExponent(self) -> int:
        """
        Cython signature: int getFinalMSExponent()
        Returns the final MS exponent
        """
        ...
    
    def setFinalMSExponent(self, final_MS_exponent: int ) -> None:
        """
        Cython signature: void setFinalMSExponent(int final_MS_exponent)
        Sets the final MS exponent
        """
        ...
    
    def getMagneticFieldStrength(self) -> float:
        """
        Cython signature: double getMagneticFieldStrength()
        Returns the strength of the magnetic field (in T)
        """
        ...
    
    def setMagneticFieldStrength(self, magnetic_field_strength: float ) -> None:
        """
        Cython signature: void setMagneticFieldStrength(double magnetic_field_strength)
        Sets the strength of the magnetic field (in T)
        """
        ...
    
    def getOrder(self) -> int:
        """
        Cython signature: int getOrder()
        Returns the position of this part in the whole Instrument
        """
        ...
    
    def setOrder(self, order: int ) -> None:
        """
        Cython signature: void setOrder(int order)
        Sets the order
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
    
    def __richcmp__(self, other: MassAnalyzer, op: int) -> Any:
        ...
    AnalyzerType : __AnalyzerType
    ReflectronState : __ReflectronState
    ResolutionMethod : __ResolutionMethod
    ResolutionType : __ResolutionType
    ScanDirection : __ScanDirection
    ScanLaw : __ScanLaw 


class MetaboliteFeatureDeconvolution:
    """
    Cython implementation of _MetaboliteFeatureDeconvolution

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MetaboliteFeatureDeconvolution.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MetaboliteFeatureDeconvolution()
        """
        ...
    
    @overload
    def __init__(self, in_0: MetaboliteFeatureDeconvolution ) -> None:
        """
        Cython signature: void MetaboliteFeatureDeconvolution(MetaboliteFeatureDeconvolution &)
        """
        ...
    
    def compute(self, fm_in: FeatureMap , fm_out: FeatureMap , cons_map: ConsensusMap , cons_map_p: ConsensusMap ) -> None:
        """
        Cython signature: void compute(FeatureMap & fm_in, FeatureMap & fm_out, ConsensusMap & cons_map, ConsensusMap & cons_map_p)
        Compute a zero-charge feature map from a set of charged features
        
        Find putative ChargePairs, then score them and hand over to ILP
        
        
        :param fm_in: Input feature-map
        :param fm_out: Output feature-map (sorted by position and augmented with user params)
        :param cons_map: Output of grouped features belonging to a charge group
        :param cons_map_p: Output of paired features connected by an edge
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
    CHARGEMODE_MFD : __CHARGEMODE_MFD 


class MorpheusScore:
    """
    Cython implementation of _MorpheusScore

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MorpheusScore.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MorpheusScore()
        """
        ...
    
    @overload
    def __init__(self, in_0: MorpheusScore ) -> None:
        """
        Cython signature: void MorpheusScore(MorpheusScore &)
        """
        ...
    
    def compute(self, fragment_mass_tolerance: float , fragment_mass_tolerance_unit_ppm: bool , exp_spectrum: MSSpectrum , theo_spectrum: MSSpectrum ) -> MorpheusScore_Result:
        """
        Cython signature: MorpheusScore_Result compute(double fragment_mass_tolerance, bool fragment_mass_tolerance_unit_ppm, const MSSpectrum & exp_spectrum, const MSSpectrum & theo_spectrum)
        Returns Morpheus Score
        """
        ... 


class MorpheusScore_Result:
    """
    Cython implementation of _MorpheusScore_Result

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MorpheusScore_Result.html>`_
    """
    
    matches: int
    
    n_peaks: int
    
    score: float
    
    MIC: float
    
    TIC: float
    
    err: float
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MorpheusScore_Result()
        """
        ...
    
    @overload
    def __init__(self, in_0: MorpheusScore_Result ) -> None:
        """
        Cython signature: void MorpheusScore_Result(MorpheusScore_Result &)
        """
        ... 


class MultiplexDeltaMasses:
    """
    Cython implementation of _MultiplexDeltaMasses

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MultiplexDeltaMasses.html>`_

    Data structure for mass shift pattern
    
    Groups of labelled peptides appear with characteristic mass shifts
    
    For example, for an Arg6 labeled SILAC peptide pair we expect to see
    mass shifts of 0 and 6 Da. Or as second example, for a
    peptide pair of a dimethyl labelled sample with a single lysine
    we will see mass shifts of 56 Da and 64 Da.
    28 Da (N-term) + 28 Da (K) and 34 Da (N-term) + 34 Da (K)
    for light and heavy partners respectively
    
    The data structure stores the mass shifts and corresponding labels
    for a group of matching peptide features
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void MultiplexDeltaMasses()
        """
        ...
    
    @overload
    def __init__(self, in_0: MultiplexDeltaMasses ) -> None:
        """
        Cython signature: void MultiplexDeltaMasses(MultiplexDeltaMasses &)
        """
        ...
    
    @overload
    def __init__(self, dm: List[MultiplexDeltaMasses_DeltaMass] ) -> None:
        """
        Cython signature: void MultiplexDeltaMasses(libcpp_vector[MultiplexDeltaMasses_DeltaMass] & dm)
        """
        ...
    
    def getDeltaMasses(self) -> List[MultiplexDeltaMasses_DeltaMass]:
        """
        Cython signature: libcpp_vector[MultiplexDeltaMasses_DeltaMass] getDeltaMasses()
        """
        ... 


class MultiplexDeltaMasses_DeltaMass:
    """
    Cython implementation of _MultiplexDeltaMasses_DeltaMass

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1MultiplexDeltaMasses_DeltaMass.html>`_
    """
    
    delta_mass: float
    
    @overload
    def __init__(self, dm: float , l: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void MultiplexDeltaMasses_DeltaMass(double dm, String l)
        """
        ...
    
    @overload
    def __init__(self, in_0: MultiplexDeltaMasses_DeltaMass ) -> None:
        """
        Cython signature: void MultiplexDeltaMasses_DeltaMass(MultiplexDeltaMasses_DeltaMass &)
        """
        ... 


class NucleicAcidSpectrumGenerator:
    """
    Cython implementation of _NucleicAcidSpectrumGenerator

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1NucleicAcidSpectrumGenerator.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void NucleicAcidSpectrumGenerator()
        """
        ...
    
    @overload
    def __init__(self, in_0: NucleicAcidSpectrumGenerator ) -> None:
        """
        Cython signature: void NucleicAcidSpectrumGenerator(NucleicAcidSpectrumGenerator &)
        """
        ...
    
    def getSpectrum(self, spec: MSSpectrum , oligo: NASequence , min_charge: int , max_charge: int ) -> None:
        """
        Cython signature: void getSpectrum(MSSpectrum & spec, NASequence & oligo, int min_charge, int max_charge)
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


class OPXLSpectrumProcessingAlgorithms:
    """
    Cython implementation of _OPXLSpectrumProcessingAlgorithms

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1OPXLSpectrumProcessingAlgorithms.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void OPXLSpectrumProcessingAlgorithms()
        """
        ...
    
    @overload
    def __init__(self, in_0: OPXLSpectrumProcessingAlgorithms ) -> None:
        """
        Cython signature: void OPXLSpectrumProcessingAlgorithms(OPXLSpectrumProcessingAlgorithms &)
        """
        ...
    
    def mergeAnnotatedSpectra(self, first_spectrum: MSSpectrum , second_spectrum: MSSpectrum ) -> MSSpectrum:
        """
        Cython signature: MSSpectrum mergeAnnotatedSpectra(MSSpectrum & first_spectrum, MSSpectrum & second_spectrum)
        """
        ...
    
    def preprocessSpectra(self, exp: MSExperiment , fragment_mass_tolerance: float , fragment_mass_tolerance_unit_ppm: bool , peptide_min_size: int , min_precursor_charge: int , max_precursor_charge: int , deisotope: bool , labeled: bool ) -> MSExperiment:
        """
        Cython signature: MSExperiment preprocessSpectra(MSExperiment & exp, double fragment_mass_tolerance, bool fragment_mass_tolerance_unit_ppm, size_t peptide_min_size, int min_precursor_charge, int max_precursor_charge, bool deisotope, bool labeled)
        """
        ...
    
    def getSpectrumAlignmentFastCharge(self, alignment: List[List[int, int]] , fragment_mass_tolerance: float , fragment_mass_tolerance_unit_ppm: bool , theo_spectrum: MSSpectrum , exp_spectrum: MSSpectrum , theo_charges: IntegerDataArray , exp_charges: IntegerDataArray , ppm_error_array: FloatDataArray , intensity_cutoff: float ) -> None:
        """
        Cython signature: void getSpectrumAlignmentFastCharge(libcpp_vector[libcpp_pair[size_t,size_t]] & alignment, double fragment_mass_tolerance, bool fragment_mass_tolerance_unit_ppm, const MSSpectrum & theo_spectrum, const MSSpectrum & exp_spectrum, const IntegerDataArray & theo_charges, const IntegerDataArray & exp_charges, FloatDataArray & ppm_error_array, double intensity_cutoff)
        """
        ...
    
    def getSpectrumAlignmentSimple(self, alignment: List[List[int, int]] , fragment_mass_tolerance: float , fragment_mass_tolerance_unit_ppm: bool , theo_spectrum: List[SimplePeak] , exp_spectrum: MSSpectrum , exp_charges: IntegerDataArray ) -> None:
        """
        Cython signature: void getSpectrumAlignmentSimple(libcpp_vector[libcpp_pair[size_t,size_t]] & alignment, double fragment_mass_tolerance, bool fragment_mass_tolerance_unit_ppm, const libcpp_vector[SimplePeak] & theo_spectrum, const MSSpectrum & exp_spectrum, const IntegerDataArray & exp_charges)
        """
        ... 


class OPXL_PreprocessedPairSpectra:
    """
    Cython implementation of _OPXL_PreprocessedPairSpectra

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::OPXLDataStructs_1_1OPXL_PreprocessedPairSpectra.html>`_
    """
    
    spectra_linear_peaks: MSExperiment
    
    spectra_xlink_peaks: MSExperiment
    
    spectra_all_peaks: MSExperiment
    
    @overload
    def __init__(self, size: int ) -> None:
        """
        Cython signature: void OPXL_PreprocessedPairSpectra(size_t size)
        """
        ...
    
    @overload
    def __init__(self, in_0: OPXL_PreprocessedPairSpectra ) -> None:
        """
        Cython signature: void OPXL_PreprocessedPairSpectra(OPXL_PreprocessedPairSpectra &)
        """
        ... 


class OSWFile:
    """
    Cython implementation of _OSWFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1OSWFile.html>`_

    This class serves for reading in and writing OpenSWATH OSW files
    
    See OpenSwathOSWWriter for more functionality
    
    The reader and writer returns data in a format suitable for PercolatorAdapter.
    OSW files have a flexible data structure. They contain all peptide query
    parameters of TraML/PQP files with the detected and quantified features of
    OpenSwathWorkflow (feature, feature_ms1, feature_ms2 & feature_transition)
    
    The OSWFile reader extracts the feature information from the OSW file for
    each level (MS1, MS2 & transition) separately and generates Percolator input
    files. For each of the three Percolator reports, OSWFile writer adds a table
    (score_ms1, score_ms2, score_transition) with the respective confidence metrics.
    These tables can be mapped to the corresponding feature tables, are very similar
    to PyProphet results and can thus be used interchangeably
    """
    
    @overload
    def __init__(self, filename: Union[bytes, str] ) -> None:
        """
        Cython signature: void OSWFile(const libcpp_utf8_string filename)
        """
        ...
    
    @overload
    def __init__(self, in_0: OSWFile ) -> None:
        """
        Cython signature: void OSWFile(OSWFile &)
        """
        ... 


class OptimizationFunctions_PenaltyFactors:
    """
    Cython implementation of _OptimizationFunctions_PenaltyFactors

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1OptimizationFunctions_PenaltyFactors.html>`_
    """
    
    pos: float
    
    lWidth: float
    
    rWidth: float
    
    def __init__(self) -> None:
        """
        Cython signature: void OptimizationFunctions_PenaltyFactors()
        """
        ... 


class OptimizePick:
    """
    Cython implementation of _OptimizePick

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1OptimizePick.html>`_

    This class provides the non-linear optimization of the peak parameters
    
    Given a vector of peak shapes, this class optimizes all peak shapes parameters using a non-linear optimization
    For the non-linear optimization we use the Levenberg-Marquardt algorithm provided by the Eigen
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void OptimizePick()
        """
        ...
    
    @overload
    def __init__(self, in_0: OptimizePick ) -> None:
        """
        Cython signature: void OptimizePick(OptimizePick &)
        """
        ...
    
    @overload
    def __init__(self, penalties_: OptimizationFunctions_PenaltyFactors , max_iteration_: int ) -> None:
        """
        Cython signature: void OptimizePick(OptimizationFunctions_PenaltyFactors penalties_, int max_iteration_)
        """
        ...
    
    def getPenalties(self) -> OptimizationFunctions_PenaltyFactors:
        """
        Cython signature: OptimizationFunctions_PenaltyFactors getPenalties()
        Returns the penalty factors
        """
        ...
    
    def setPenalties(self, penalties: OptimizationFunctions_PenaltyFactors ) -> None:
        """
        Cython signature: void setPenalties(OptimizationFunctions_PenaltyFactors penalties)
        Sets the penalty factors
        """
        ...
    
    def getNumberIterations(self) -> int:
        """
        Cython signature: unsigned int getNumberIterations()
        Returns the number of iterations
        """
        ...
    
    def setNumberIterations(self, max_iteration: int ) -> None:
        """
        Cython signature: void setNumberIterations(int max_iteration)
        Sets the number of iterations
        """
        ... 


class OptimizePick_Data:
    """
    Cython implementation of _OptimizePick_Data

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1OptimizePick_Data.html>`_
    """
    
    positions: List[float]
    
    signal: List[float] 


class Param:
    """
    Cython implementation of _Param

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1Param.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void Param()
        """
        ...
    
    @overload
    def __init__(self, in_0: Param ) -> None:
        """
        Cython signature: void Param(Param &)
        """
        ...
    
    @overload
    def setValue(self, key: Union[bytes, str] , val: Union[int, float, bytes, str, List[int], List[float], List[bytes]] , desc: Union[bytes, str] , tags: List[Union[bytes, str]] ) -> None:
        """
        Cython signature: void setValue(libcpp_utf8_string key, ParamValue val, libcpp_utf8_string desc, libcpp_vector[libcpp_utf8_string] tags)
        """
        ...
    
    @overload
    def setValue(self, key: Union[bytes, str] , val: Union[int, float, bytes, str, List[int], List[float], List[bytes]] , desc: Union[bytes, str] ) -> None:
        """
        Cython signature: void setValue(libcpp_utf8_string key, ParamValue val, libcpp_utf8_string desc)
        """
        ...
    
    @overload
    def setValue(self, key: Union[bytes, str] , val: Union[int, float, bytes, str, List[int], List[float], List[bytes]] ) -> None:
        """
        Cython signature: void setValue(libcpp_utf8_string key, ParamValue val)
        """
        ...
    
    def getValue(self, key: Union[bytes, str] ) -> Union[int, float, bytes, str, List[int], List[float], List[bytes]]:
        """
        Cython signature: ParamValue getValue(libcpp_utf8_string key)
        """
        ...
    
    def getValueType(self, key: Union[bytes, str] ) -> int:
        """
        Cython signature: ValueType getValueType(libcpp_utf8_string key)
        """
        ...
    
    def getEntry(self, in_0: Union[bytes, str] ) -> ParamEntry:
        """
        Cython signature: ParamEntry getEntry(libcpp_utf8_string)
        """
        ...
    
    def exists(self, key: Union[bytes, str] ) -> bool:
        """
        Cython signature: bool exists(libcpp_utf8_string key)
        """
        ...
    
    def addTag(self, key: Union[bytes, str] , tag: Union[bytes, str] ) -> None:
        """
        Cython signature: void addTag(libcpp_utf8_string key, libcpp_utf8_string tag)
        """
        ...
    
    def addTags(self, key: Union[bytes, str] , tags: List[Union[bytes, str]] ) -> None:
        """
        Cython signature: void addTags(libcpp_utf8_string key, libcpp_vector[libcpp_utf8_string] tags)
        """
        ...
    
    def hasTag(self, key: Union[bytes, str] , tag: Union[bytes, str] ) -> int:
        """
        Cython signature: int hasTag(libcpp_utf8_string key, libcpp_utf8_string tag)
        """
        ...
    
    def getTags(self, key: Union[bytes, str] ) -> List[bytes]:
        """
        Cython signature: libcpp_vector[libcpp_string] getTags(libcpp_utf8_string key)
        """
        ...
    
    def clearTags(self, key: Union[bytes, str] ) -> None:
        """
        Cython signature: void clearTags(libcpp_utf8_string key)
        """
        ...
    
    def getDescription(self, key: Union[bytes, str] ) -> str:
        """
        Cython signature: libcpp_utf8_output_string getDescription(libcpp_utf8_string key)
        """
        ...
    
    def setSectionDescription(self, key: Union[bytes, str] , desc: Union[bytes, str] ) -> None:
        """
        Cython signature: void setSectionDescription(libcpp_utf8_string key, libcpp_utf8_string desc)
        """
        ...
    
    def getSectionDescription(self, key: Union[bytes, str] ) -> str:
        """
        Cython signature: libcpp_utf8_output_string getSectionDescription(libcpp_utf8_string key)
        """
        ...
    
    def addSection(self, key: Union[bytes, str] , desc: Union[bytes, str] ) -> None:
        """
        Cython signature: void addSection(libcpp_utf8_string key, libcpp_utf8_string desc)
        """
        ...
    
    def size(self) -> int:
        """
        Cython signature: size_t size()
        """
        ...
    
    def empty(self) -> bool:
        """
        Cython signature: bool empty()
        """
        ...
    
    def clear(self) -> None:
        """
        Cython signature: void clear()
        """
        ...
    
    def insert(self, prefix: Union[bytes, str] , param: Param ) -> None:
        """
        Cython signature: void insert(libcpp_utf8_string prefix, Param param)
        """
        ...
    
    def remove(self, key: Union[bytes, str] ) -> None:
        """
        Cython signature: void remove(libcpp_utf8_string key)
        """
        ...
    
    def removeAll(self, prefix: Union[bytes, str] ) -> None:
        """
        Cython signature: void removeAll(libcpp_utf8_string prefix)
        """
        ...
    
    @overload
    def copy(self, prefix: Union[bytes, str] , in_1: bool ) -> Param:
        """
        Cython signature: Param copy(libcpp_utf8_string prefix, bool)
        """
        ...
    
    @overload
    def copy(self, prefix: Union[bytes, str] ) -> Param:
        """
        Cython signature: Param copy(libcpp_utf8_string prefix)
        """
        ...
    
    def merge(self, toMerge: Param ) -> None:
        """
        Cython signature: void merge(Param toMerge)
        """
        ...
    
    @overload
    def setDefaults(self, defaults: Param , prefix: Union[bytes, str] , showMessage: bool ) -> None:
        """
        Cython signature: void setDefaults(Param defaults, libcpp_utf8_string prefix, bool showMessage)
        """
        ...
    
    @overload
    def setDefaults(self, defaults: Param , prefix: Union[bytes, str] ) -> None:
        """
        Cython signature: void setDefaults(Param defaults, libcpp_utf8_string prefix)
        """
        ...
    
    @overload
    def setDefaults(self, defaults: Param ) -> None:
        """
        Cython signature: void setDefaults(Param defaults)
        """
        ...
    
    @overload
    def checkDefaults(self, name: Union[bytes, str] , defaults: Param , prefix: Union[bytes, str] ) -> None:
        """
        Cython signature: void checkDefaults(libcpp_utf8_string name, Param defaults, libcpp_utf8_string prefix)
        """
        ...
    
    @overload
    def checkDefaults(self, name: Union[bytes, str] , defaults: Param ) -> None:
        """
        Cython signature: void checkDefaults(libcpp_utf8_string name, Param defaults)
        """
        ...
    
    def setValidStrings(self, key: Union[bytes, str] , strings: List[Union[bytes, str]] ) -> None:
        """
        Cython signature: void setValidStrings(libcpp_utf8_string key, libcpp_vector[libcpp_utf8_string] strings)
        """
        ...
    
    def setMinInt(self, key: Union[bytes, str] , min: int ) -> None:
        """
        Cython signature: void setMinInt(libcpp_utf8_string key, int min)
        """
        ...
    
    def setMaxInt(self, key: Union[bytes, str] , max: int ) -> None:
        """
        Cython signature: void setMaxInt(libcpp_utf8_string key, int max)
        """
        ...
    
    def setMinFloat(self, key: Union[bytes, str] , min: float ) -> None:
        """
        Cython signature: void setMinFloat(libcpp_utf8_string key, double min)
        """
        ...
    
    def setMaxFloat(self, key: Union[bytes, str] , max: float ) -> None:
        """
        Cython signature: void setMaxFloat(libcpp_utf8_string key, double max)
        """
        ...
    
    def __richcmp__(self, other: Param, op: int) -> Any:
        ... 


class Peak1D:
    """
    Cython implementation of _Peak1D

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1Peak1D.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void Peak1D()
        """
        ...
    
    @overload
    def __init__(self, in_0: Peak1D ) -> None:
        """
        Cython signature: void Peak1D(Peak1D &)
        """
        ...
    
    def getIntensity(self) -> float:
        """
        Cython signature: float getIntensity()
        """
        ...
    
    def getMZ(self) -> float:
        """
        Cython signature: double getMZ()
        """
        ...
    
    def setMZ(self, in_0: float ) -> None:
        """
        Cython signature: void setMZ(double)
        """
        ...
    
    def setIntensity(self, in_0: float ) -> None:
        """
        Cython signature: void setIntensity(float)
        """
        ...
    
    def getPos(self) -> float:
        """
        Cython signature: double getPos()
        """
        ...
    
    def setPos(self, pos: float ) -> None:
        """
        Cython signature: void setPos(double pos)
        """
        ...
    
    def __richcmp__(self, other: Peak1D, op: int) -> Any:
        ... 


class PeakIndex:
    """
    Cython implementation of _PeakIndex

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakIndex.html>`_

    Index of a peak or feature
    
    This struct can be used to store both peak or feature indices
    """
    
    peak: int
    
    spectrum: int
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void PeakIndex()
        """
        ...
    
    @overload
    def __init__(self, in_0: PeakIndex ) -> None:
        """
        Cython signature: void PeakIndex(PeakIndex &)
        """
        ...
    
    @overload
    def __init__(self, peak: int ) -> None:
        """
        Cython signature: void PeakIndex(size_t peak)
        """
        ...
    
    @overload
    def __init__(self, spectrum: int , peak: int ) -> None:
        """
        Cython signature: void PeakIndex(size_t spectrum, size_t peak)
        """
        ...
    
    def isValid(self) -> bool:
        """
        Cython signature: bool isValid()
        Returns if the current peak ref is valid
        """
        ...
    
    def clear(self) -> None:
        """
        Cython signature: void clear()
        Invalidates the current index
        """
        ...
    
    def getFeature(self, map_: FeatureMap ) -> Feature:
        """
        Cython signature: Feature getFeature(FeatureMap & map_)
        Returns the feature (or consensus feature) corresponding to this index
        
        This method is intended for arrays of features e.g. FeatureMap
        
        The main advantage of using this method instead accessing the data directly is that range
        check performed in debug mode
        
        :raises:
          Exception: Precondition is thrown if this index is invalid for the `map` (only in debug mode)
        """
        ...
    
    def getPeak(self, map_: MSExperiment ) -> Peak1D:
        """
        Cython signature: Peak1D getPeak(MSExperiment & map_)
        Returns a peak corresponding to this index
        
        This method is intended for arrays of DSpectra e.g. MSExperiment
        
        The main advantage of using this method instead accessing the data directly is that range
        check performed in debug mode
        
        :raises:
          Exception: Precondition is thrown if this index is invalid for the `map` (only in debug mode)
        """
        ...
    
    def getSpectrum(self, map_: MSExperiment ) -> MSSpectrum:
        """
        Cython signature: MSSpectrum getSpectrum(MSExperiment & map_)
        Returns a spectrum corresponding to this index
        
        This method is intended for arrays of DSpectra e.g. MSExperiment
        
        The main advantage of using this method instead accessing the data directly is that range
        check performed in debug mode
        
        :raises:
          Exception: Precondition is thrown if this index is invalid for the `map` (only in debug mode)
        """
        ...
    
    def __richcmp__(self, other: PeakIndex, op: int) -> Any:
        ... 


class ProtonDistributionModel:
    """
    Cython implementation of _ProtonDistributionModel

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ProtonDistributionModel.html>`_
      -- Inherits from ['DefaultParamHandler']

    A proton distribution model to calculate the proton distribution over charged peptides
    
    The model uses proton affinity values of backbone nitrogens and sidechains to calculate the
    proton distribution of charged peptide among these sites. The possible sites are the peptide
    bonds between the amino acids, the side chains and the C-terminus and N-terminus. The calculation
    is done calculating a Boltzmann distribution of the sites
    
    Details and the proton affinities can be found in
    Z. Zhang, Prediction of Low-Energy Collision-Induced Dissociation Spectra of Peptides,
    Anal. Chem., 76 (14), 3908 - 3922, 2004
    
    A proton distribution can be calculated using the getProtonDistribution method. The backbone
    probabilities are reported in the first parameter (index 0 for the N-terminus, index 1 for the
    first peptide bond...), the site chain probabilities are reported in the second parameter
    (index 0, for the first amino acid...). The peptide and the number of protons as well as type
    of peptide (can be Reside::YIon for peptides and y-ions and any other ion type)
    
    Charge state intensities of differently charged equal (e.g. y7+ and y7++) ions can be calculated
    using the getChargeStateIntensities function
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ProtonDistributionModel()
        A proton distribution model to calculate the proton distribution over charged peptides
        
        The model uses proton affinity values of backbone nitrogens and sidechains to calculate the
        proton distribution of charged peptide among these sites. The possible sites are the peptide
        bonds between the amino acids, the side chains and the C-terminus and N-terminus. The calculation
        is done calculating a Boltzmann distribution of the sites
        
        Details and the proton affinities can be found in
        Z. Zhang, Prediction of Low-Energy Collision-Induced Dissociation Spectra of Peptides,
        Anal. Chem., 76 (14), 3908 - 3922, 2004
        
        A proton distribution can be calculated using the getProtonDistribution method. The backbone
        probabilities are reported in the first parameter (index 0 for the N-terminus, index 1 for the
        first peptide bond...), the site chain probabilities are reported in the second parameter
        (index 0, for the first amino acid...). The peptide and the number of protons as well as type
        of peptide (can be Reside::YIon for peptides and y-ions and any other ion type)
        
        Charge state intensities of differently charged equal (e.g. y7+ and y7++) ions can be calculated
        using the getChargeStateIntensities function
        """
        ...
    
    @overload
    def __init__(self, in_0: ProtonDistributionModel ) -> None:
        """
        Cython signature: void ProtonDistributionModel(ProtonDistributionModel &)
        """
        ...
    
    def getProtonDistribution(self, bb_charges: List[float] , sc_charges: List[float] , peptide: AASequence , charge: int , res_type: int ) -> None:
        """
        Cython signature: void getProtonDistribution(libcpp_vector[double] & bb_charges, libcpp_vector[double] & sc_charges, AASequence & peptide, int charge, ResidueType res_type)
        Calculates a proton distribution of the given charged peptide
        
        
        :param bb_charges: The calculated probabilities of the backbone sites (including N-terminus and C-terminus)
        :param sc_charges: The calculated probabilities of the side chain sites
        :param peptide: The peptide as AASequence object
        :param charge: The charge
        :param res_type: The type of the ion given in peptide. Peptides are handled as y-ions, i.e. Residue::YIon
        """
        ...
    
    def getChargeStateIntensities(self, peptide: AASequence , n_term_ion: AASequence , c_term_ion: AASequence , charge: int , n_term_type: int , n_term_intensities: List[float] , c_term_intensities: List[float] , type_: int ) -> None:
        """
        Cython signature: void getChargeStateIntensities(AASequence & peptide, AASequence & n_term_ion, AASequence & c_term_ion, int charge, ResidueType n_term_type, libcpp_vector[double] & n_term_intensities, libcpp_vector[double] & c_term_intensities, FragmentationType type_)
        Calculates the charge state intensities of different charge states of the same ion
        
        
        :param peptide: The peptide
        :param n_term_ion: The prefix ion sequence
        :param c_term_ion: The suffix ion sequence
        :param charge: The charge
        :param n_term_type: The ion type of the N-terminal ion; valid values are Residue::AIon, Residue::BIon
        :param n_term_intensities: The probability of seeing a charged prefix ions (first index corresponds to ion of charge 1)
        :param c_term_intensities: The probability of seeing a charged suffix ions (first index corresponds to ion of charge 2)
        :param type: The type of fragmentation (charge-directed, charge-remote of side chain)
        """
        ...
    
    def setPeptideProtonDistribution(self, bb_charge: List[float] , sc_charge: List[float] ) -> None:
        """
        Cython signature: void setPeptideProtonDistribution(libcpp_vector[double] & bb_charge, libcpp_vector[double] & sc_charge)
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
    FragmentationType : __FragmentationType 


class QTCluster:
    """
    Cython implementation of _QTCluster

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1QTCluster.html>`_
    """
    
    def __init__(self, in_0: QTCluster ) -> None:
        """
        Cython signature: void QTCluster(QTCluster &)
        """
        ...
    
    def getCenterRT(self) -> float:
        """
        Cython signature: double getCenterRT()
        Returns the RT value of the cluster
        """
        ...
    
    def getCenterMZ(self) -> float:
        """
        Cython signature: double getCenterMZ()
        Returns the m/z value of the cluster center
        """
        ...
    
    def getXCoord(self) -> int:
        """
        Cython signature: int getXCoord()
        Returns the x coordinate in the grid
        """
        ...
    
    def getYCoord(self) -> int:
        """
        Cython signature: int getYCoord()
        Returns the y coordinate in the grid
        """
        ...
    
    def size(self) -> int:
        """
        Cython signature: size_t size()
        Returns the size of the cluster (number of elements, incl. center)
        """
        ...
    
    def getQuality(self) -> float:
        """
        Cython signature: double getQuality()
        Returns the cluster quality and recomputes if necessary
        """
        ...
    
    def getAnnotations(self) -> Set[AASequence]:
        """
        Cython signature: libcpp_set[AASequence] getAnnotations()
        Returns the set of peptide sequences annotated to the cluster center
        """
        ...
    
    def setInvalid(self) -> None:
        """
        Cython signature: void setInvalid()
        Sets current cluster as invalid (also frees some memory)
        """
        ...
    
    def isInvalid(self) -> bool:
        """
        Cython signature: bool isInvalid()
        Whether current cluster is invalid
        """
        ...
    
    def initializeCluster(self) -> None:
        """
        Cython signature: void initializeCluster()
        Has to be called before adding elements (calling
        """
        ...
    
    def finalizeCluster(self) -> None:
        """
        Cython signature: void finalizeCluster()
        Has to be called after adding elements (after calling
        """
        ...
    
    def __richcmp__(self, other: QTCluster, op: int) -> Any:
        ... 


class ResidueDB:
    """
    Cython implementation of _ResidueDB

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ResidueDB.html>`_
    """
    
    def getNumberOfResidues(self) -> int:
        """
        Cython signature: size_t getNumberOfResidues()
        Returns the number of residues stored
        """
        ...
    
    def getNumberOfModifiedResidues(self) -> int:
        """
        Cython signature: size_t getNumberOfModifiedResidues()
        Returns the number of modified residues stored
        """
        ...
    
    def getResidue(self, name: Union[bytes, str, String] ) -> Residue:
        """
        Cython signature: const Residue * getResidue(const String & name)
        Returns a pointer to the residue with name, 3 letter code or 1 letter code name
        """
        ...
    
    @overload
    def getModifiedResidue(self, name: Union[bytes, str, String] ) -> Residue:
        """
        Cython signature: const Residue * getModifiedResidue(const String & name)
        Returns a pointer to a modified residue given a modification name
        """
        ...
    
    @overload
    def getModifiedResidue(self, residue: Residue , name: Union[bytes, str, String] ) -> Residue:
        """
        Cython signature: const Residue * getModifiedResidue(Residue * residue, const String & name)
        Returns a pointer to a modified residue given a residue and a modification name
        """
        ...
    
    def getResidues(self, residue_set: Union[bytes, str, String] ) -> Set[Residue]:
        """
        Cython signature: libcpp_set[const Residue *] getResidues(const String & residue_set)
        Returns a set of all residues stored in this residue db
        """
        ...
    
    def getResidueSets(self) -> Set[bytes]:
        """
        Cython signature: libcpp_set[String] getResidueSets()
        Returns all residue sets that are registered which this instance
        """
        ...
    
    def hasResidue(self, name: Union[bytes, str, String] ) -> bool:
        """
        Cython signature: bool hasResidue(const String & name)
        Returns true if the db contains a residue with the given name
        """
        ... 


class SiriusAdapterIdentification:
    """
    Cython implementation of _SiriusAdapterIdentification

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS::SiriusMzTabWriter_1_1SiriusAdapterIdentification.html>`_
    """
    
    mz: float
    
    rt: float
    
    native_ids: List[bytes]
    
    scan_index: int
    
    scan_number: int
    
    feature_id: Union[bytes, str, String]
    
    hits: List[SiriusAdapterHit]
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void SiriusAdapterIdentification()
        """
        ...
    
    @overload
    def __init__(self, in_0: SiriusAdapterIdentification ) -> None:
        """
        Cython signature: void SiriusAdapterIdentification(SiriusAdapterIdentification &)
        """
        ... 


class SpectrumAccessOpenMSCached:
    """
    Cython implementation of _SpectrumAccessOpenMSCached

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumAccessOpenMSCached.html>`_
      -- Inherits from ['ISpectrumAccess']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void SpectrumAccessOpenMSCached()
        """
        ...
    
    @overload
    def __init__(self, filename: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void SpectrumAccessOpenMSCached(String filename)
        An implementation of the Spectrum Access interface using on-disk caching
        
        This class implements the OpenSWATH Spectrum Access interface
        (ISpectrumAccess) using the CachedmzML class which is able to read and
        write a cached mzML file
        """
        ...
    
    @overload
    def __init__(self, in_0: SpectrumAccessOpenMSCached ) -> None:
        """
        Cython signature: void SpectrumAccessOpenMSCached(SpectrumAccessOpenMSCached &)
        """
        ...
    
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


class SpectrumSettings:
    """
    Cython implementation of _SpectrumSettings

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumSettings.html>`_
      -- Inherits from ['MetaInfoInterface']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void SpectrumSettings()
        """
        ...
    
    @overload
    def __init__(self, in_0: SpectrumSettings ) -> None:
        """
        Cython signature: void SpectrumSettings(SpectrumSettings &)
        """
        ...
    
    def unify(self, in_0: SpectrumSettings ) -> None:
        """
        Cython signature: void unify(SpectrumSettings)
        """
        ...
    
    def getType(self) -> int:
        """
        Cython signature: int getType()
        Returns the spectrum type (centroided (PEAKS) or profile data (RAW))
        """
        ...
    
    def setType(self, in_0: int ) -> None:
        """
        Cython signature: void setType(SpectrumType)
        Sets the spectrum type
        """
        ...
    
    def getNativeID(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getNativeID()
        Returns the native identifier for the spectrum, used by the acquisition software
        """
        ...
    
    def setNativeID(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setNativeID(String)
        Sets the native identifier for the spectrum, used by the acquisition software
        """
        ...
    
    def getComment(self) -> Union[bytes, str, String]:
        """
        Cython signature: String getComment()
        Returns the free-text comment
        """
        ...
    
    def setComment(self, in_0: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void setComment(String)
        Sets the free-text comment
        """
        ...
    
    def getInstrumentSettings(self) -> InstrumentSettings:
        """
        Cython signature: InstrumentSettings getInstrumentSettings()
        Returns a const reference to the instrument settings of the current spectrum
        """
        ...
    
    def setInstrumentSettings(self, in_0: InstrumentSettings ) -> None:
        """
        Cython signature: void setInstrumentSettings(InstrumentSettings)
        Sets the instrument settings of the current spectrum
        """
        ...
    
    def getAcquisitionInfo(self) -> AcquisitionInfo:
        """
        Cython signature: AcquisitionInfo getAcquisitionInfo()
        Returns a const reference to the acquisition info
        """
        ...
    
    def setAcquisitionInfo(self, in_0: AcquisitionInfo ) -> None:
        """
        Cython signature: void setAcquisitionInfo(AcquisitionInfo)
        Sets the acquisition info
        """
        ...
    
    def getSourceFile(self) -> SourceFile:
        """
        Cython signature: SourceFile getSourceFile()
        Returns a const reference to the source file
        """
        ...
    
    def setSourceFile(self, in_0: SourceFile ) -> None:
        """
        Cython signature: void setSourceFile(SourceFile)
        Sets the source file
        """
        ...
    
    def getPrecursors(self) -> List[Precursor]:
        """
        Cython signature: libcpp_vector[Precursor] getPrecursors()
        Returns a const reference to the precursors
        """
        ...
    
    def setPrecursors(self, in_0: List[Precursor] ) -> None:
        """
        Cython signature: void setPrecursors(libcpp_vector[Precursor])
        Sets the precursors
        """
        ...
    
    def getProducts(self) -> List[Product]:
        """
        Cython signature: libcpp_vector[Product] getProducts()
        Returns a const reference to the products
        """
        ...
    
    def setProducts(self, in_0: List[Product] ) -> None:
        """
        Cython signature: void setProducts(libcpp_vector[Product])
        Sets the products
        """
        ...
    
    def getPeptideIdentifications(self) -> List[PeptideIdentification]:
        """
        Cython signature: libcpp_vector[PeptideIdentification] getPeptideIdentifications()
        Returns a const reference to the PeptideIdentification vector
        """
        ...
    
    def setPeptideIdentifications(self, in_0: List[PeptideIdentification] ) -> None:
        """
        Cython signature: void setPeptideIdentifications(libcpp_vector[PeptideIdentification])
        Sets the PeptideIdentification vector
        """
        ...
    
    def getDataProcessing(self) -> List[DataProcessing]:
        """
        Cython signature: libcpp_vector[shared_ptr[DataProcessing]] getDataProcessing()
        """
        ...
    
    def setDataProcessing(self, in_0: List[DataProcessing] ) -> None:
        """
        Cython signature: void setDataProcessing(libcpp_vector[shared_ptr[DataProcessing]])
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
    
    def __richcmp__(self, other: SpectrumSettings, op: int) -> Any:
        ...
    SpectrumType : __SpectrumType 


class String:
    """
    Cython implementation of _String

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1String.html>`_
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void String()
        """
        ...
    
    def __richcmp__(self, other: String, op: int) -> Any:
        ... 


class SwathWindowLoader:
    """
    Cython implementation of _SwathWindowLoader

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1SwathWindowLoader.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void SwathWindowLoader()
        """
        ...
    
    @overload
    def __init__(self, in_0: SwathWindowLoader ) -> None:
        """
        Cython signature: void SwathWindowLoader(SwathWindowLoader &)
        """
        ...
    
    def annotateSwathMapsFromFile(self, filename: Union[bytes, str, String] , swath_maps: List[SwathMap] , do_sort: bool , force: bool ) -> None:
        """
        Cython signature: void annotateSwathMapsFromFile(String filename, libcpp_vector[SwathMap] & swath_maps, bool do_sort, bool force)
        """
        ...
    
    def readSwathWindows(self, filename: Union[bytes, str, String] , swath_prec_lower: List[float] , swath_prec_upper: List[float] ) -> None:
        """
        Cython signature: void readSwathWindows(String filename, libcpp_vector[double] & swath_prec_lower, libcpp_vector[double] & swath_prec_upper)
        """
        ... 


class TICFilter:
    """
    Cython implementation of _TICFilter

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1TICFilter.html>`_
      -- Inherits from ['FilterFunctor']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void TICFilter()
        """
        ...
    
    @overload
    def __init__(self, in_0: TICFilter ) -> None:
        """
        Cython signature: void TICFilter(TICFilter &)
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


class TM_DataPoint:
    """
    Cython implementation of _TM_DataPoint

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1TM_DataPoint.html>`_
    """
    
    first: float
    
    second: float
    
    note: Union[bytes, str, String]
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void TM_DataPoint()
        """
        ...
    
    @overload
    def __init__(self, in_0: float , in_1: float ) -> None:
        """
        Cython signature: void TM_DataPoint(double, double)
        """
        ...
    
    @overload
    def __init__(self, in_0: float , in_1: float , in_2: Union[bytes, str, String] ) -> None:
        """
        Cython signature: void TM_DataPoint(double, double, const String &)
        """
        ...
    
    def __richcmp__(self, other: TM_DataPoint, op: int) -> Any:
        ... 


class ThresholdMower:
    """
    Cython implementation of _ThresholdMower

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1ThresholdMower.html>`_
      -- Inherits from ['DefaultParamHandler']
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void ThresholdMower()
        """
        ...
    
    @overload
    def __init__(self, in_0: ThresholdMower ) -> None:
        """
        Cython signature: void ThresholdMower(ThresholdMower &)
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


class TraceInfo:
    """
    Cython implementation of _TraceInfo

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1TraceInfo.html>`_
    """
    
    name: bytes
    
    description: bytes
    
    opened: bool
    
    @overload
    def __init__(self, n: Union[bytes, str] , d: Union[bytes, str] , o: bool ) -> None:
        """
        Cython signature: void TraceInfo(libcpp_utf8_string n, libcpp_utf8_string d, bool o)
        """
        ...
    
    @overload
    def __init__(self, in_0: TraceInfo ) -> None:
        """
        Cython signature: void TraceInfo(TraceInfo)
        """
        ... 


class TransformationModelLinear:
    """
    Cython implementation of _TransformationModelLinear

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1TransformationModelLinear.html>`_
      -- Inherits from ['TransformationModel']
    """
    
    def __init__(self, data: List[TM_DataPoint] , params: Param ) -> None:
        """
        Cython signature: void TransformationModelLinear(libcpp_vector[TM_DataPoint] & data, Param & params)
        """
        ...
    
    def evaluate(self, value: float ) -> float:
        """
        Cython signature: double evaluate(double value)
        """
        ...
    
    def invert(self) -> None:
        """
        Cython signature: void invert()
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
    
    getDefaultParameters: __static_TransformationModelLinear_getDefaultParameters 


class XTandemXMLFile:
    """
    Cython implementation of _XTandemXMLFile

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classOpenMS_1_1XTandemXMLFile.html>`_
    """
    
    def __init__(self) -> None:
        """
        Cython signature: void XTandemXMLFile()
        """
        ...
    
    def load(self, filename: Union[bytes, str, String] , protein_identification: ProteinIdentification , id_data: List[PeptideIdentification] , mod_def_set: ModificationDefinitionsSet ) -> None:
        """
        Cython signature: void load(String filename, ProteinIdentification & protein_identification, libcpp_vector[PeptideIdentification] & id_data, ModificationDefinitionsSet & mod_def_set)
        """
        ... 


class streampos:
    """
    Cython implementation of _streampos

    Original C++ documentation is available `here <http://www.openms.de/current_doxygen/html/classstd_1_1streampos.html>`_
    """
    
    @overload
    def __init__(self, ) -> None:
        """
        Cython signature: void streampos()
        """
        ...
    
    @overload
    def __init__(self, in_0: streampos ) -> None:
        """
        Cython signature: void streampos(streampos &)
        """
        ... 


class __AnalyzerType:
    None
    ANALYZERNULL : int
    QUADRUPOLE : int
    PAULIONTRAP : int
    RADIALEJECTIONLINEARIONTRAP : int
    AXIALEJECTIONLINEARIONTRAP : int
    TOF : int
    SECTOR : int
    FOURIERTRANSFORM : int
    IONSTORAGE : int
    ESA : int
    IT : int
    SWIFT : int
    CYCLOTRON : int
    ORBITRAP : int
    LIT : int
    SIZE_OF_ANALYZERTYPE : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class AnnotationState:
    None
    FEATURE_ID_NONE : int
    FEATURE_ID_SINGLE : int
    FEATURE_ID_MULTIPLE_SAME : int
    FEATURE_ID_MULTIPLE_DIVERGENT : int
    SIZE_OF_ANNOTATIONSTATE : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __CHARGEMODE_MFD:
    None
    QFROMFEATURE : int
    QHEURISTIC : int
    QALL : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __FragmentationType:
    None
    ChargeDirected : int
    ChargeRemote : int
    SideChain : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __InletType:
    None
    INLETNULL : int
    DIRECT : int
    BATCH : int
    CHROMATOGRAPHY : int
    PARTICLEBEAM : int
    MEMBRANESEPARATOR : int
    OPENSPLIT : int
    JETSEPARATOR : int
    SEPTUM : int
    RESERVOIR : int
    MOVINGBELT : int
    MOVINGWIRE : int
    FLOWINJECTIONANALYSIS : int
    ELECTROSPRAYINLET : int
    THERMOSPRAYINLET : int
    INFUSION : int
    CONTINUOUSFLOWFASTATOMBOMBARDMENT : int
    INDUCTIVELYCOUPLEDPLASMA : int
    MEMBRANE : int
    NANOSPRAY : int
    SIZE_OF_INLETTYPE : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __IonizationMethod:
    None
    IONMETHODNULL : int
    ESI : int
    EI : int
    CI : int
    FAB : int
    TSP : int
    LD : int
    FD : int
    FI : int
    PD : int
    SI : int
    TI : int
    API : int
    ISI : int
    CID : int
    CAD : int
    HN : int
    APCI : int
    APPI : int
    ICP : int
    NESI : int
    MESI : int
    SELDI : int
    SEND : int
    FIB : int
    MALDI : int
    MPI : int
    DI : int
    FA : int
    FII : int
    GD_MS : int
    NICI : int
    NRMS : int
    PI : int
    PYMS : int
    REMPI : int
    AI : int
    ASI : int
    AD : int
    AUI : int
    CEI : int
    CHEMI : int
    DISSI : int
    LSI : int
    PEI : int
    SOI : int
    SPI : int
    SUI : int
    VI : int
    AP_MALDI : int
    SILI : int
    SALDI : int
    SIZE_OF_IONIZATIONMETHOD : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class NormalizationMethod:
    None
    NM_SCALE : int
    NM_SHIFT : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __Polarity:
    None
    POLNULL : int
    POSITIVE : int
    NEGATIVE : int
    SIZE_OF_POLARITY : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class QuotingMethod:
    None
    NONE : int
    ESCAPE : int
    DOUBLE : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __ReflectronState:
    None
    REFLSTATENULL : int
    ON : int
    OFF : int
    NONE : int
    SIZE_OF_REFLECTRONSTATE : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __ResolutionMethod:
    None
    RESMETHNULL : int
    FWHM : int
    TENPERCENTVALLEY : int
    BASELINE : int
    SIZE_OF_RESOLUTIONMETHOD : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __ResolutionType:
    None
    RESTYPENULL : int
    CONSTANT : int
    PROPORTIONAL : int
    SIZE_OF_RESOLUTIONTYPE : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __ScanDirection:
    None
    SCANDIRNULL : int
    UP : int
    DOWN : int
    SIZE_OF_SCANDIRECTION : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __ScanLaw:
    None
    SCANLAWNULL : int
    EXPONENTIAL : int
    LINEAR : int
    QUADRATIC : int
    SIZE_OF_SCANLAW : int

    def getMapping(self) -> Dict[int, str]:
       ... 


class __SpectrumType:
    None
    UNKNOWN : int
    CENTROID : int
    PROFILE : int
    SIZE_OF_SPECTRUMTYPE : int

    def getMapping(self) -> Dict[int, str]:
       ... 

