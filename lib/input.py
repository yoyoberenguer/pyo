from _core import *

######################################################################
### Sources
######################################################################                                       
class Sine(PyoObject):
    """
    A simple oscillator.
    
    **Parameters**
    
    freq : float or PyoObject, optional
        Frequency in cycles per second. Default to 1000.
    phase : float or PyoObject, optional
        Phase of sampling, expressed as a fraction of a cycle (0 to 1). Default to 0.
        
    **Methods**
    
    setFreq(x) : Replace the `freq` attribute.
    setPhase(x) : Replace the `phase` attribute.
    
    """
    def __init__(self, freq=1000, phase=0, mul=1, add=0):
        self._freq = freq
        self._phase = phase
        self._mul = mul
        self._add = add
        freq, phase, mul, add, lmax = convertArgsToLists(freq, phase, mul, add)
        self._base_objs = [Sine_base(wrap(freq,i), wrap(phase,i), wrap(mul,i), wrap(add,i)) for i in range(lmax)]

    def setFreq(self, x):
        """Replace the `freq` attribute.
        
        **Parameters**

        x : float or PyoObject
            new `freq` attribute.
        
        """
        self._freq = x
        x, lmax = convertArgsToLists(x)
        [obj.setFreq(wrap(x,i)) for i, obj in enumerate(self._base_objs)]
        
    def setPhase(self, x):
        """Replace the `phase` attribute.
        
        **Parameters**

        x : float or PyoObject
            new `phase` attribute.
        
        """
        self._phase = x
        x, lmax = convertArgsToLists(x)
        [obj.setPhase(wrap(x,i)) for i, obj in enumerate(self._base_objs)]

    def demo():
        execfile("demos/Sine_demo.py")
    demo = Call_example(demo)
        
    @property
    def freq(self): return self._freq
    @property
    def phase(self): return self._phase
    @freq.setter
    def freq(self, x): self.setFreq(x)
    @phase.setter
    def phase(self, x): self.setPhase(x)
 
class Osc(PyoObject):
    """
    A simple oscillator with linear interpolation reading a waveform table.
    
    **Parameters**
    
    table : PyoTableObject
        Table containing the waveform samples.
    freq : float or PyoObject, optional
        Frequency in cycles per second. Default to 1000.
    phase : float or PyoObject, optional
        Phase of sampling, expressed as a fraction of a cycle (0 to 1). Default to 0.
        
    **Methods**
    
    setFreq(x) : Replace the `freq` attribute.
    setPhase(x) : Replace the `phase` attribute.
    
    """
    def __init__(self, table, freq=1000, phase=0, mul=1, add=0):
        self._table = table
        self._freq = freq
        self._phase = phase
        self._mul = mul
        self._add = add
        table, freq, phase, mul, add, lmax = convertArgsToLists(table, freq, phase, mul, add)
        self._base_objs = [Osc_base(wrap(table,i), wrap(freq,i), wrap(phase,i), wrap(mul,i), wrap(add,i)) for i in range(lmax)]

    def setFreq(self, x):
        """Replace the `freq` attribute.
        
        **Parameters**

        x : float or PyoObject
            new `freq` attribute.
        
        """
        self._freq = x
        x, lmax = convertArgsToLists(x)
        [obj.setFreq(wrap(x,i)) for i, obj in enumerate(self._base_objs)]

    def setPhase(self, x):
        """Replace the `phase` attribute.
        
        **Parameters**

        x : float or PyoObject
            new `phase` attribute.
        
        """
        self._phase = x
        x, lmax = convertArgsToLists(x)
        [obj.setPhase(wrap(x,i)) for i, obj in enumerate(self._base_objs)]

    def demo():
        execfile("demos/Osc_demo.py")
    demo = Call_example(demo)

    @property
    def freq(self): return self._freq
    @property
    def phase(self): return self._phase
    @freq.setter
    def freq(self, x): self.setFreq(x)
    @phase.setter
    def phase(self, x): self.setPhase(x)

class Input(PyoObject):
    """
    Reads from a numbered channel in an external audio signal or stream.
    
    **Parameters**
    
    chnl : int, optional
        Input channel to read from. Default to 0.
    
    """
    def __init__(self, chnl=0, mul=1, add=0):                
        self._chnl = chnl
        self._mul = mul
        self._add = add
        chnl, mul, add, lmax = convertArgsToLists(chnl, mul, add)
        self._base_objs = [Input_base(wrap(chnl,i), wrap(mul,i), wrap(add,i)) for i in range(lmax)]

class Noise(PyoObject):
    def __init__(self, mul=1, add=0):                
        """
        A white noise generator.
        
        """
        self._mul = mul
        self._add = add
        mul, add, lmax = convertArgsToLists(mul, add)
        self._base_objs = [Noise_base(wrap(mul,i), wrap(add,i)) for i in range(lmax)]