#!/usr/bin/env python3
import numpy as np
from scipy.special import comb

def likelihood(x, n, P):
    # 1. Kontrol: n pozitif bir tam sayı mı?
    if not isinstance(n, (int, np.integer)) or n <= 0:
        raise ValueError("n must be a positive integer")
        
    # 2. Kontrol: x sıfırdan büyük veya eşit bir tam sayı mı?
    if not isinstance(x, (int, np.integer)) or x < 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")
        
    # 3. Kontrol: x, n'den büyük mü?
    if x > n:
        raise ValueError("x cannot be greater than n")
        
    # 4. Kontrol: P bir 1D numpy dizisi mi?
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
        
    # 5. Kontrol: P'deki tüm değerler [0, 1] aralığında mı?
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
        
    # --- Hesaplama Kısmı ---
    # Kombinasyon hesaplama: n'in x'li kombinasyonu
    # (n ve x sabit olduğu için tek bir sayı üretecek)
    kombinasyon = comb(n, x)
    
    # Binom formülünün uygulanması:
    # P bir numpy dizisi olduğu için, işlemler eleman bazlı (element-wise) otomatik yapılır.
    olabilirlik = kombinasyon * (P ** x) * ((1 - P) ** (n - x))
    
    return olabilirlik