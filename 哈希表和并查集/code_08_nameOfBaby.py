#coding:utf-8
'''
@Time: 2020/3/22 22:50
@author: Tokyo
@file: code_08_nameOfBaby.py
@desc:
每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。

在结果列表中，选择字典序最小的名字作为真实名字。

示例：

输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
输出：["John(27)","Chris(36)"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/baby-names-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Element():
    def __init__(self, val):
        self.val = val


class UnionFindSet():
    def __init__(self, arr):
        self.elementMap = {}
        self.fatherMap = {}
        self.sizeMap = {}
        for i in arr:
            ele = Element(i[0])
            self.fatherMap[ele] = ele
            self.elementMap[i[0]] = ele
            self.sizeMap[ele] = i[1]

    def findHead(self, a):
        if a in self.elementMap:
            ele = self.elementMap[a]
            stack = []
            while ele != self.fatherMap[ele]:
                stack.append(ele)
                ele = self.fatherMap[ele]
            while stack != []:
                self.fatherMap[stack.pop()] = ele
            return ele

    def isSameSet(self, a, b):
        if a in self.elementMap and b in self.elementMap:
            if self.findHead(a) == self.findHead(b):
                return True
        return False

    def Union(self, a, b):
        if a in self.elementMap and b in self.elementMap:
            if not self.isSameSet(a, b):
                aF = self.findHead(a)
                bF = self.findHead(b)
                # 这里要根据场景改，不是比较a和b的字典序哦！
                # 应该比较a和b的father的字典序
                big = aF if aF.val < bF.val else bF
                small = bF if big == aF else aF
                self.fatherMap[small] = big
                self.sizeMap[big] += self.sizeMap[small]
                self.sizeMap.pop(small)


def trulyMostPopular(names,synonyms):
    if names == []:
        return []
    fine = []
    for i in names:
        p = i.find('(')
        name = i[:p]
        num = int(i[p + 1:-1])

        fine.append([name, num])
    pp = UnionFindSet(fine)
    for i in synonyms:
        i = i[1:-1].split(',')
        pp.Union(i[0], i[1])

    res = []
    for k, v in pp.sizeMap.items():
        res.append(str(k.val) + '(' + str(v) + ')')
    return res


if __name__ == '__main__':
    names = ["Fcclu(70)","Ommjh(63)","Dnsay(60)","Qbmk(45)","Unsb(26)","Gauuk(75)","Wzyyim(34)","Bnea(55)","Kri(71)","Qnaakk(76)","Gnplfi(68)","Hfp(97)","Qoi(70)","Ijveol(46)","Iidh(64)","Qiy(26)","Mcnef(59)","Hvueqc(91)","Obcbxb(54)","Dhe(79)","Jfq(26)","Uwjsu(41)","Wfmspz(39)","Ebov(96)","Ofl(72)","Uvkdpn(71)","Avcp(41)","Msyr(9)","Pgfpma(95)","Vbp(89)","Koaak(53)","Qyqifg(85)","Dwayf(97)","Oltadg(95)","Mwwvj(70)","Uxf(74)","Qvjp(6)","Grqrg(81)","Naf(3)","Xjjol(62)","Ibink(32)","Qxabri(41)","Ucqh(51)","Mtz(72)","Aeax(82)","Kxutz(5)","Qweye(15)","Ard(82)","Chycnm(4)","Hcvcgc(97)","Knpuq(61)","Yeekgc(11)","Ntfr(70)","Lucf(62)","Uhsg(23)","Csh(39)","Txixz(87)","Kgabb(80)","Weusps(79)","Nuq(61)","Drzsnw(87)","Xxmsn(98)","Onnev(77)","Owh(64)","Fpaf(46)","Hvia(6)","Kufa(95)","Chhmx(66)","Avmzs(39)","Okwuq(96)","Hrschk(30)","Ffwni(67)","Wpagta(25)","Npilye(14)","Axwtno(57)","Qxkjt(31)","Dwifi(51)","Kasgmw(95)","Vgxj(11)","Nsgbth(26)","Nzaz(51)","Owk(87)","Yjc(94)","Hljt(21)","Jvqg(47)","Alrksy(69)","Tlv(95)","Acohsf(86)","Qejo(60)","Gbclj(20)","Nekuam(17)","Meutux(64)","Tuvzkd(85)","Fvkhz(98)","Rngl(12)","Gbkq(77)","Uzgx(65)","Ghc(15)","Qsc(48)","Siv(47)"]
    b = ["(Gnplfi,Qxabri)","(Uzgx,Siv)","(Bnea,Lucf)","(Qnaakk,Msyr)","(Grqrg,Gbclj)","(Uhsg,Qejo)","(Csh,Wpagta)","(Xjjol,Lucf)","(Qoi,Obcbxb)","(Npilye,Vgxj)","(Aeax,Ghc)","(Txixz,Ffwni)","(Qweye,Qsc)","(Kri,Tuvzkd)","(Ommjh,Vbp)","(Pgfpma,Xxmsn)","(Uhsg,Csh)","(Qvjp,Kxutz)","(Qxkjt,Tlv)","(Wfmspz,Owk)","(Dwayf,Chycnm)","(Iidh,Qvjp)","(Dnsay,Rngl)","(Qweye,Tlv)","(Wzyyim,Kxutz)","(Hvueqc,Qejo)","(Tlv,Ghc)","(Hvia,Fvkhz)","(Msyr,Owk)","(Hrschk,Hljt)","(Owh,Gbclj)","(Dwifi,Uzgx)","(Iidh,Fpaf)","(Iidh,Meutux)","(Txixz,Ghc)","(Gbclj,Qsc)","(Kgabb,Tuvzkd)","(Uwjsu,Grqrg)","(Vbp,Dwayf)","(Xxmsn,Chhmx)","(Uxf,Uzgx)"]
    c = trulyMostPopular(names,b)
    rightans = ["Fcclu(70)","Dnsay(72)","Qbmk(45)","Unsb(26)","Gauuk(75)","Gnplfi(109)","Hfp(97)","Obcbxb(124)","Ijveol(46)","Fpaf(219)","Qiy(26)","Mcnef(59)","Dhe(79)","Jfq(26)","Ebov(96)","Ofl(72)","Uvkdpn(71)","Avcp(41)","Chycnm(253)","Koaak(53)","Qyqifg(85)","Oltadg(95)","Mwwvj(70)","Naf(3)","Ibink(32)","Ucqh(51)","Mtz(72)","Ard(82)","Hcvcgc(97)","Knpuq(61)","Yeekgc(11)","Ntfr(70)","Bnea(179)","Weusps(79)","Nuq(61)","Drzsnw(87)","Chhmx(259)","Onnev(77)","Kufa(95)","Avmzs(39)","Okwuq(96)","Hljt(51)","Npilye(25)","Axwtno(57)","Kasgmw(95)","Nsgbth(26)","Nzaz(51)","Msyr(211)","Yjc(94)","Jvqg(47)","Alrksy(69)","Aeax(646)","Acohsf(86)","Csh(238)","Nekuam(17)","Kgabb(236)","Fvkhz(104)","Gbkq(77)","Dwifi(237)"]
