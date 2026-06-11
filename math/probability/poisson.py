#!/usr/bin/env python3
class Poisson:
    """Class that represents a poisson distribution."""

    def __init__(self, data=None, lambtha=1.):
        """ The function represents a poisson distribution."""
        if data is None:
            # data is not given, controlling lambtha. 
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            # data is given
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            
            # Lambda = mean 
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of 'successes'.
        """
       
        k = int(k)

       
        if k < 0:
            return 0

       
        e = 2.7182818285

        
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i

        
        lambtha_power_k = self.lambtha ** k
        e_power_lambtha = e ** self.lambtha

        pmf_value = lambtha_power_k / (e_power_lambtha * factorial)

        return pmf_value
    
    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of 'successes'.
        """
        k = int(k)

        if k < 0:
            return 0

        e = 2.7182818285
        lambtha = self.lambtha
        total_cdf = 0.0
        factorial = 1

        
        for i in range(k + 1):
            if i > 0:
                factorial *= i

            lambtha_power_i = lambtha ** i
            e_power_lambtha = e ** lambtha
            pmf_i = lambtha_power_i / (e_power_lambtha * factorial)

            total_cdf += pmf_i

        return total_cdf
    