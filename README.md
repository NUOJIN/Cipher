#密码学  
   这是一个有关密码学的rep库，内容包括了最基础的凯撒加密法及其破解代码，换位加密法及其破解代码，仿射加密法及其破解代码，简单替代加密法及其破解代码，维吉尼亚加密法及其破解代码以及现在所广泛使用的RSA加密法。参考书本为Albert Sweigart的《python密码学编程》.  
##凯撒加密法  
###加密  
是最基础的加密方法，可以用轮盘或滑条实现。详见文件caesar_cipher.py
###破解  
通过26种逐次暴力破解。详见文件 caesar_cipher.py
##换位加密法  
###加密  
利用调换文字横纵向顺序进行加密，横向字符数量为密匙。详见文件 transposition_swap.py
###破解  
换位加密法的暴力破解需要引入 dictionary.txt 文件以及 isEnglish 函数:
<pre><code>  
def isEnglish(message,wordPercentage=20,letterPercentage=85):
    wordsMatch = getEnglishCount(message)*100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters)/len(message)*100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch  
</code></pre>  
凭借 isEnglish函数 对多次暴力破解结果进行判断，从而实现对换位加密法的破解。详见文件 transpositonHacker.py
##仿射加密法  
###加密  
仿射加密法可以理解为一种复杂的二重凯撒加密，通过加法和乘法的混合实现了解密难度的提高，从而提升了加密效率。仿射加密法详见文件 affineCipher.py  
###破解  
虽然难度增加了很多，但仿射加密法仍然是可以破解的。破解复杂度和 len(LETTERS) 的平方相当。详见文件 affineHacker.py  
##简单替代加密法  
###加密  
简单替代加密法通过增加密匙的复杂度，使得其破译难度大大提高。详见文件 simpleSubCipher.py
###破解  
简单替代加密法由于破解算法复杂度过大，已经不适合暴力破解。我们在这里通过获取密词的候选单词列表，构造字符间的一一对应关系，从而实现最终的破解。对于简单替代加密法，待破解的字符串越长，破解难度越小。详见文件 simpleSubHacker.py  
##维吉尼亚加密法  
###加密  
维尼吉亚加密法是一种复杂化的凯撒加密法，它的密匙由单词或不规则字母组合构成。由于其不可避免的复杂性，维尼吉亚加密法曾经号称“不可破译的加密法”。详见文件 vinegereCipher.py
###破解  
##RSA加密法  
###加密