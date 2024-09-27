import unittest
from spellChecker import check, load_corpus, check_real_word_error


class spellCheckerTest(unittest.TestCase):
    
    #Test correct words
    def test_1(self):
        testWord = "hawdd"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_2(self):
        testWord = "dehongli"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_3(self):
        testWord = "pêl"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
    
    def test_4(self):
        testWord = "corfforol"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_5(self):
        testWord = "awyren"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_6(self):
        testWord = "efallai"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_7(self):
        testWord = "ffidil"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_8(self):
        testWord = "adnewyddadwy"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_9(self):
        testWord = "awyrgylch"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_10(self):
        testWord = "lletchwith"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_11(self):
        testWord = "ebargofiant"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_12(self):
        testWord = "arbrofi"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
    
    def test_13(self):
        testWord = "hanner"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_14(self):
        testWord = "rhwng"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_15(self):
        testWord = "cyson"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_16(self):
        testWord = "enghreifftiau"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_17(self):
        testWord = "llawen"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_18(self):
        testWord = "amserlen"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_19(self):
        testWord = "rhuthro"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_20(self):
        testWord = "melin"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
        
    def test_21(self):
        testWord = "boneddigion"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
        
    def test_22(self):
        testWord = "calon"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_23(self):
        testWord = "cenedlaethol"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
    
    def test_24(self):
        testWord = "gorau"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_25(self):
        testWord = "fferm"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
    
    def test_26(self):
        testWord = "marchnad"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_27(self):
        testWord = "disglair"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_28(self):
        testWord = "desg"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_29(self):
        testWord = "dydd"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_30(self):
        testWord = "brenhines"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_31(self):
        testWord = "gwely"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_32(self):
        testWord = "hiraeth"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_33(self):
        testWord = "hwyr"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_34(self):
        testWord = "ieithoedd"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_35(self):
        testWord = "ifanc"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_36(self):
        testWord = "hafan"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_37(self):
        testWord = "cynefin"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_38(self):
        testWord = "gorsaf"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_39(self):
        testWord = "gweithio"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_40(self):
        testWord = "gwasanaeth"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)

    def test_41(self):
        testWord = "chwarae"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_42(self):
        testWord = "chwerw"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_43(self):
        testWord = "llyfr"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_44(self):
        testWord = "llefaru"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_45(self):
        testWord = "llawr"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_46(self):
        testWord = "gwrych"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_47(self):
        testWord = "enwog"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_48(self):
        testWord = "potel"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_49(self):
        testWord = "bwrdd"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    def test_50(self):
        testWord = "adar"
        result = "Word is spelled correctly"
        self.assertEqual(check(testWord), result)
        
    
    #Test whether incorrect words of Levenshtein distance 1 have the correct suggestion
    def test_51(self):
        testWord = "anpdd"
        self.assertIn("anodd", check(testWord))
        
    def test_52(self):
        testWord = "hawdq"
        self.assertIn("hawdd", check(testWord))
        
    def test_53(self):
        testWord = "adnewyddadww"
        self.assertIn("adnewyddadwy", check(testWord))
        
    def test_54(self):
        testWord = "ples"
        self.assertIn("pres", check(testWord))
    
    def test_55(self):
        testWord = "prian"
        self.assertIn("arian", check(testWord))
        
    def test_56(self):
        testWord = "awb"
        self.assertIn("pawb", check(testWord))
        
    def test_57(self):
        testWord = "mwen"
        self.assertIn("mewn", check(testWord))
    
    def test_58(self):
        testWord = "anfiail"
        self.assertIn("anifail", check(testWord))
     
    def test_59(self):
        testWord = "cymdeitas"
        self.assertIn("cymdeithas", check(testWord))
        
    def test_60(self):
        testWord = "eglwyes"
        self.assertIn("eglwys", check(testWord))
    
    def test_61(self):
        testWord = "gwybodawth"
        self.assertIn("gwybodaeth", check(testWord))
        
    def test_62(self):
        testWord = "ago"
        self.assertIn("agos", check(testWord))
        
    def test_63(self):
        testWord = "gwelli"
        self.assertIn("gwella", check(testWord))
        
    def test_64(self):
        testWord = "esgidiua"
        self.assertIn("esgidiau", check(testWord))
    
    def test_65(self):
        testWord = "gosdo"
        self.assertIn("gosod", check(testWord))
        
    def test_66(self):
        testWord = "drwsa"
        self.assertIn("drws", check(testWord))
        
    def test_67(self):
        testWord = "cr"
        self.assertIn("car", check(testWord))
    
    def test_68(self):
        testWord = "hellynt"
        self.assertIn("helynt", check(testWord))
     
    def test_69(self):
        testWord = "gwalt"
        self.assertIn("gwallt", check(testWord))
        
    def test_70(self):
        testWord = "nso"
        self.assertIn("nos", check(testWord))
        
    def test_71(self):
        testWord = "ffpn"
        self.assertIn("ffon", check(testWord))
        
    def test_72(self):
        testWord = "haln"
        self.assertIn("halen", check(testWord))
        
    def test_73(self):
        testWord = "nefoewd"
        self.assertIn("nefoedd", check(testWord))
        
    def test_74(self):
        testWord = "tp"
        self.assertIn("tŷ", check(testWord))
    
    def test_75(self):
        testWord = "terlu"
        self.assertIn("teulu", check(testWord))
        
    def test_76(self):
        testWord = "ffried"
        self.assertIn("ffrind", check(testWord))
        
    def test_77(self):
        testWord = "mwsof"
        self.assertIn("mwsog", check(testWord))
    
    def test_78(self):
        testWord = "chweck"
        self.assertIn("chwech", check(testWord))
     
    def test_79(self):
        testWord = "saetg"
        self.assertIn("saeth", check(testWord))
        
    def test_80(self):
        testWord = "aderwn"
        self.assertIn("aderyn", check(testWord))
        
    def test_81(self):
        testWord = "coeedn"
        self.assertIn("coeden", check(testWord))
        
    def test_82(self):
        testWord = "mahemateg"
        self.assertIn("mathemateg", check(testWord))
        
    def test_83(self):
        testWord = "bafarn"
        self.assertIn("tafarn", check(testWord))
        
    def test_84(self):
        testWord = "canofan"
        self.assertIn("canolfan", check(testWord))
    
    def test_85(self):
        testWord = "cymed"
        self.assertIn("cymedr", check(testWord))
        
    def test_86(self):
        testWord = "glaswelt"
        self.assertIn("glaswellt", check(testWord))
        
    def test_87(self):
        testWord = "mwnyhau"
        self.assertIn("mwynhau", check(testWord))
    
    def test_88(self):
        testWord = "cerddde"
        self.assertIn("cerdded", check(testWord))
     
    def test_89(self):
        testWord = "tren"
        self.assertIn("trên", check(testWord))
        
    def test_90(self):
        testWord = "anl"
        self.assertIn("aml", check(testWord))
        
    def test_91(self):
        testWord = "pryhnawn"
        self.assertIn("prynhawn", check(testWord))
        
    def test_92(self):
        testWord = "hedddiw"
        self.assertIn("heddiw", check(testWord))
        
    def test_93(self):
        testWord = "mynsd"
        self.assertIn("mynd", check(testWord))
        
    def test_94(self):
        testWord = "gorwewl"
        self.assertIn("gorwel", check(testWord))
    
    def test_95(self):
        testWord = "lalwn"
        self.assertIn("llawn", check(testWord))
        
    def test_96(self):
        testWord = "gwyne"
        self.assertIn("gwynt", check(testWord))
        
    def test_97(self):
        testWord = "tywdd"
        self.assertIn("tywydd", check(testWord))
    
    def test_98(self):
        testWord = "cymre"
        self.assertIn("cymru", check(testWord))
     
    def test_99(self):
        testWord = "ffordw"
        self.assertIn("ffordd", check(testWord))
        
    def test_100(self):
        testWord = "pae"
        self.assertIn("pam", check(testWord))
        
    
    #Test whether incorrect words of Levenshtein distance 2 have the correct suggestion
    def test_101(self):
        testWord = "myunoi"
        self.assertIn("ymuno", check(testWord))
    
    def test_102(self):
        testWord = "hedich"
        self.assertIn("heddwch", check(testWord))
        
    def test_103(self):
        testWord = "cllun"
        self.assertIn("cynllun", check(testWord))
        
    def test_104(self):
        testWord = "tyrdyd"
        self.assertIn("trydydd", check(testWord))
        
    def test_105(self):
        testWord = "annnwyb"
        self.assertIn("annwyl", check(testWord))
        
    def test_106(self):
        testWord = "paarto"
        self.assertIn("paratoi", check(testWord))
        
    def test_107(self):
        testWord = "achlysd"
        self.assertIn("achlysur", check(testWord))
        
    def test_108(self):
        testWord = "ardwr"
        self.assertIn("arfer", check(testWord))
        
    def test_109(self):
        testWord = "gahanor"
        self.assertIn("gwahanol", check(testWord))
        
    def test_110(self):
        testWord = "ystafeik"
        self.assertIn("ystafell", check(testWord))
        
    def test_111(self):
        testWord = "ysl"
        self.assertIn("ysgol", check(testWord))
    
    def test_112(self):
        testWord = "ymwalwar"
        self.assertIn("ymwelwyr", check(testWord))
        
    def test_113(self):
        testWord = "mwybdool"
        self.assertIn("ymwybodol", check(testWord))
        
    def test_114(self):
        testWord = "mlade"
        self.assertIn("ymladd", check(testWord))
        
    def test_115(self):
        testWord = "aymlean"
        self.assertIn("ymlaen", check(testWord))
        
    def test_116(self):
        testWord = "ong"
        self.assertIn("llong", check(testWord))
        
    def test_117(self):
        testWord = "caairn"
        self.assertIn("cadair", check(testWord))
        
    def test_118(self):
        testWord = "teydna"
        self.assertIn("trydan", check(testWord))
        
    def test_119(self):
        testWord = "gweadw"
        self.assertIn("gwaed", check(testWord))
        
    def test_120(self):
        testWord = "glwybs"
        self.assertIn("gwlyb", check(testWord))
        
    def test_121(self):
        testWord = "myunoi"
        self.assertIn("ymuno", check(testWord))
    
    def test_122(self):
        testWord = "diloc"
        self.assertIn("diolch", check(testWord))
        
    def test_123(self):
        testWord = "rwng"
        self.assertIn("drwg", check(testWord))
        
    def test_124(self):
        testWord = "pewda"
        self.assertIn("pedwar", check(testWord))
        
    def test_125(self):
        testWord = "gwanyne"
        self.assertIn("gwanwyn", check(testWord))
        
    def test_126(self):
        testWord = "hyrfe"
        self.assertIn("hydref", check(testWord))
        
    def test_127(self):
        testWord = "ieran"
        self.assertIn("eira", check(testWord))
        
    def test_128(self):
        testWord = "canurs"
        self.assertIn("canu", check(testWord))
        
    def test_129(self):
        testWord = "hredegi"
        self.assertIn("rhedeg", check(testWord))
        
    def test_130(self):
        testWord = "prifygso"
        self.assertIn("prifysgol", check(testWord))
        
    def test_131(self):
        testWord = "efny"
        self.assertIn("cefn", check(testWord))
    
    def test_132(self):
        testWord = "uwhcbwn"
        self.assertIn("uwchben", check(testWord))
        
    def test_133(self):
        testWord = "elpi"
        self.assertIn("helpu", check(testWord))
        
    def test_134(self):
        testWord = "rhannnu"
        self.assertIn("rhannu", check(testWord))
        
    def test_135(self):
        testWord = "cfi"
        self.assertIn("cofio", check(testWord))
        
    def test_136(self):
        testWord = "enil"
        self.assertIn("ennill", check(testWord))
        
    def test_137(self):
        testWord = "ryndw"
        self.assertIn("mynd", check(testWord))
        
    def test_138(self):
        testWord = "custadly"
        self.assertIn("cystadlu", check(testWord))
        
    def test_139(self):
        testWord = "deaile"
        self.assertIn("deall", check(testWord))
        
    def test_140(self):
        testWord = "soarda"
        self.assertIn("siarad", check(testWord))
        
    def test_141(self):
        testWord = "lygda"
        self.assertIn("llygad", check(testWord))
    
    def test_142(self):
        testWord = "gwepp"
        self.assertIn("gwell", check(testWord))
        
    def test_143(self):
        testWord = "cllawerp"
        self.assertIn("llawer", check(testWord))
        
    def test_144(self):
        testWord = "hywlo"
        self.assertIn("hwyl", check(testWord))
        
    def test_145(self):
        testWord = "cymdiethan"
        self.assertIn("cymdeithas", check(testWord))
        
    def test_146(self):
        testWord = "bohcr"
        self.assertIn("ochr", check(testWord))
        
    def test_147(self):
        testWord = "ieuenctaedi"
        self.assertIn("ieuenctid", check(testWord))
        
    def test_148(self):
        testWord = "gwyddiaeth"
        self.assertIn("gwyddoniaeth", check(testWord))
        
    def test_149(self):
        testWord = "cyfrifaudr"
        self.assertIn("cyfrifiadur", check(testWord))
        
    def test_150(self):
        testWord = "gwurs"
        self.assertIn("gwres", check(testWord))
        
    #Test trigrams
    def test_151(self):
        self.assertEqual(check_real_word_error("awyr", "un", "wyntog"), "yn")
        
    def test_152(self):
        self.assertEqual(check_real_word_error("fel", "yn", "mae"), "y")
        
    def test_153(self):
        self.assertEqual(check_real_word_error("gan", "gynnwys", "chwarae"), "gynnwys")
        
    def test_154(self):
        self.assertEqual(check_real_word_error("mae'r", "iaith", "gymraeg"), "iaith")
        
    def test_155(self):
        self.assertEqual(check_real_word_error("mae'r", "haul", "yn"), "haul")
        
    def test_156(self):
        self.assertEqual(check_real_word_error("haul", "yn", "codi"), "yn")
        
    def test_157(self):
        self.assertEqual(check_real_word_error("codi", "ar", "y"), "ar")
        
    def test_158(self):
        self.assertEqual(check_real_word_error("ar", "y", "gorwel"), "y")
           
    def test_159(self):
        self.assertEqual(check_real_word_error("Dw", "i", "eisiau"), "i")
        
    def test_160(self):
        self.assertEqual(check_real_word_error("i", "eisiau", "mynd"), "eisiau")
        
    def test_161(self):
        self.assertEqual(check_real_word_error("eisiau", "mynd", "i'r"), "mynd")
        
    def test_162(self):
        self.assertEqual(check_real_word_error("mynd", "i'r", "sinema"), "i'r")
        
    def test_163(self):
        self.assertEqual(check_real_word_error("i'r", "sinema", "heno"), "sinema")
        
    def test_164(self):
        self.assertEqual(check_real_word_error("mae'r", "tywydd", "yn"), "tywydd")
        
    def test_165(self):
        self.assertEqual(check_real_word_error("tywydd", "yn", "wlyb"), "yn")
        
    def test_166(self):
        self.assertEqual(check_real_word_error("mae'r", "tafarn", "yn"), "tafarn")
        
    def test_167(self):
        self.assertEqual(check_real_word_error("tafarn", "yn", "llawn"), "yn")
        
    def test_168(self):
        self.assertEqual(check_real_word_error("bydd", "y", "siopau"), "y")
           
    def test_169(self):
        self.assertEqual(check_real_word_error("y", "siopau", "yn"), "siopau")
        
    def test_170(self):
        self.assertEqual(check_real_word_error("siopau", "yn", "cau"), "yn")
                         
    def test_171(self):
        self.assertEqual(check_real_word_error("yn", "cau", "am"), "cau")
        
    def test_172(self):
        self.assertEqual(check_real_word_error("cau", "am", "naw"), "am")
        
    def test_173(self):
        self.assertEqual(check_real_word_error("am", "naw", "o'r"), "naw")
        
    def test_174(self):
        self.assertEqual(check_real_word_error("naw", "o'r", "gloch"), "o'r")
        
    def test_175(self):
        self.assertEqual(check_real_word_error("mae'r", "ardal", "yn"), "ardal")
        
    def test_176(self):
        self.assertEqual(check_real_word_error("ardal", "yn", "llawn"), "yn")
        
    def test_177(self):
        self.assertEqual(check_real_word_error("yn", "llawn", "o"), "llawn")
        
    def test_178(self):
        self.assertEqual(check_real_word_error("llawn", "o", "hanes"), "o")
           
    def test_179(self):
        self.assertEqual(check_real_word_error("mae'r", "iaith", "gymraeg"), "iaith")
        
    def test_180(self):
        self.assertEqual(check_real_word_error("iaith", "gymraeg", "yn"), "gymraeg")
                         
    def test_181(self):
        self.assertEqual(check_real_word_error("gymraeg", "yn", "cael"), "yn")
        
    def test_182(self):
        self.assertEqual(check_real_word_error("yn", "cael", "ei"), "cael")
        
    def test_183(self):
        self.assertEqual(check_real_word_error("cael", "ei", "dysgu"), "ei")
        
    def test_184(self):
        self.assertEqual(check_real_word_error("ei", "dysgu", "mewn"), "dysgu")
        
    def test_185(self):
        self.assertEqual(check_real_word_error("dysgu", "mewn", "ysgolion"), "mewn")
        
    def test_186(self):
        self.assertEqual(check_real_word_error("mewn", "ysgolion", "ledled"), "ysgolion")
        
    def test_187(self):
        self.assertEqual(check_real_word_error("ysgolion", "ledled", "cymru"), "ledled")
        
    def test_188(self):
        self.assertEqual(check_real_word_error("mae'r", "bwyd", "yn"), "bwyd")
           
    def test_189(self):
        self.assertEqual(check_real_word_error("bwyd", "yn", "flasus"), "yn")
        
    def test_190(self):
        self.assertEqual(check_real_word_error("mae'r", "castell", "yn"), "castell")
    
    def test_191(self):
        self.assertEqual(check_real_word_error("castell", "yn", "hynod"), "yn")
        
    def test_192(self):
        self.assertEqual(check_real_word_error("yn", "hynod", "o"), "hynod")
        
    def test_193(self):
        self.assertEqual(check_real_word_error("hynod", "o", "hanesyddol"), "o")
        
    def test_194(self):
        self.assertEqual(check_real_word_error("mae'r", "gogledd", "yn"), "gogledd")
        
    def test_195(self):
        self.assertEqual(check_real_word_error("gogledd", "yn", "llawn"), "yn")
        
    def test_196(self):
        self.assertEqual(check_real_word_error("yn", "llawn", "o"), "llawn")
        
    def test_197(self):
        self.assertEqual(check_real_word_error("llawn", "o", "arddangosfeydd"), "o")
        
    def test_198(self):
        self.assertEqual(check_real_word_error("o", "arddangosfeydd", "naturiol"), "arddangosfeydd")
           
    def test_199(self):
        self.assertEqual(check_real_word_error("Mae", "cerddoriaeth", "traddodiadol"), "cerddoriaeth")
        
    def test_200(self):
        self.assertEqual(check_real_word_error("cerddoriaeth", "traddodiadol", "yn"), "traddodiadol")
        
    def test_201(self):
        self.assertEqual(check_real_word_error("traddodiadol", "yn", "dal"), "yn")
        
    def test_202(self):
        self.assertEqual(check_real_word_error("yn", "dal", "i"), "dal")
        
    def test_203(self):
        self.assertEqual(check_real_word_error("dal", "i", "fod"), "i")
        
    def test_204(self):
        self.assertEqual(check_real_word_error("i", "fod", "yn"), "fod")
        
    def test_205(self):
        self.assertEqual(check_real_word_error("fod", "yn", "boblogaidd"), "yn")
        
    def test_206(self):
        self.assertEqual(check_real_word_error("yn", "boblogaidd", "hyd"), "boblogaidd")
        
    def test_207(self):
        self.assertEqual(check_real_word_error("boblogaidd", "hyd", "heddiw"), "hyd")
        
    def test_208(self):
        self.assertEqual(check_real_word_error("mae", "mwy", "o"), "mwy")
           
    def test_209(self):
        self.assertEqual(check_real_word_error("mwy", "o", "bobl"), "o")
        
    def test_210(self):
        self.assertEqual(check_real_word_error("o", "bobl", "yn"), "bobl")
        
    def test_211(self):
        self.assertEqual(check_real_word_error("bobl", "yn", "siarad"), "yn")
        
    def test_212(self):
        self.assertEqual(check_real_word_error("yn", "siarad", "saesneg"), "siarad")
        
    def test_213(self):
        self.assertEqual(check_real_word_error("siarad", "saesneg", "na"), "saesneg")
        
    def test_214(self):
        self.assertEqual(check_real_word_error("saesneg", "na", "cymraeg"), "na")
        
    def test_215(self):
        self.assertEqual(check_real_word_error("na", "cymraeg", "yng"), "cymraeg")
        
    def test_216(self):
        self.assertEqual(check_real_word_error("cymraeg", "yng", "nghymru"), "yng")
        
    def test_217(self):
        self.assertEqual(check_real_word_error("mae'r", "brawddeg", "nesaf"), "brawddeg")
        
    def test_218(self):
        self.assertEqual(check_real_word_error("brawddeg", "nesaf", "yn"), "nesaf")
           
    def test_219(self):
        self.assertEqual(check_real_word_error("nesaf", "yn", "cynnwys"), "yn")
        
    def test_220(self):
        self.assertEqual(check_real_word_error("yn", "cynnwys", "dim"), "cynnwys")
        
    def test_221(self):
        self.assertEqual(check_real_word_error("cynnwyd", "dim", "byd"), "dim")
        
    def test_222(self):
        self.assertEqual(check_real_word_error("dim", "byd", "ond"), "byd")
        
    def test_223(self):
        self.assertEqual(check_real_word_error("byd", "ond", "ffeithiau"), "ond")
        
    def test_224(self):
        self.assertEqual(check_real_word_error("pen", "blwydd", "fi"), "blwydd")
        
    def test_225(self):
        self.assertEqual(check_real_word_error("blwydd", "fi", "ydi"), "fi")
        
    def test_226(self):
        self.assertEqual(check_real_word_error("fi", "ydi", "y"), "ydi")
        
    def test_227(self):
        self.assertEqual(check_real_word_error("ydi", "mehefin", "y"), "mehefin")
        
    def test_228(self):
        self.assertEqual(check_real_word_error("mehefin", "y", "trydydd"), "y")
           
    def test_229(self):
        self.assertEqual(check_real_word_error("y", "trydydd", "ar"), "trydydd")
        
    def test_230(self):
        self.assertEqual(check_real_word_error("trydydd", "ar", "ddeg"), "ar")
                
    def test_231(self):
        self.assertEqual(check_real_word_error("gymraeg", "yn", "cael"), "ddeg")
        
    def test_232(self):
        self.assertEqual(check_real_word_error("rydw", "i'n", "hoffi"), "i'n")
        
    def test_233(self):
        self.assertEqual(check_real_word_error("i'n", "hoffi", "gwylio"), "hoffi")
        
    def test_234(self):
        self.assertEqual(check_real_word_error("hoffi", "gwylio", "rhaglennau"), "gwylio")
        
    def test_235(self):
        self.assertEqual(check_real_word_error("gwylio", "rhaglennau", "teledu"), "rhaglennau")
        
    def test_236(self):
        self.assertEqual(check_real_word_error("rhaglennau", "teledu", "yn"), "teledu")
        
    def test_237(self):
        self.assertEqual(check_real_word_error("teledu", "yn", "fy"), "yn")
        
    def test_238(self):
        self.assertEqual(check_real_word_error("yn", "fy", "amser"), "fy")
           
    def test_239(self):
        self.assertEqual(check_real_word_error("fy", "amser", "rhydd"), "amser")
        
    def test_240(self):
        self.assertEqual(check_real_word_error("mae", "hen", "wlad"), "hen")
        
    def test_241(self):
        self.assertEqual(check_real_word_error("hen", "wlad", "fy"), "wlad")
        
    def test_242(self):
        self.assertEqual(check_real_word_error("wlad", "fy", "nhadau"), "fy")
        
    def test_243(self):
        self.assertEqual(check_real_word_error("fy", "nhadau", "yn"), "nhadau")
        
    def test_244(self):
        self.assertEqual(check_real_word_error("nhadau", "yn", "annwyl"), "yn")
        
    def test_245(self):
        self.assertEqual(check_real_word_error("yn", "annwyl", "i"), "annwyl")
        
    def test_246(self):
        self.assertEqual(check_real_word_error("annwyl", "i", "mi"), "i")
        
    def test_247(self):
        self.assertEqual(check_real_word_error("ydi", "y", "profi"), "y")
        
    def test_248(self):
        self.assertEqual(check_real_word_error("y", "profi", "wedi"), "profi")
           
    def test_249(self):
        self.assertEqual(check_real_word_error("profi", "wedi", "gorffen"), "wedi")
        
    def test_250(self):
        self.assertEqual(check_real_word_error("wedi", "gorffen", "eto"), "gorffen")
    
        
#Load the corpus before running any tests
if __name__ == "__main__":
    load_corpus("biggerCorpus.txt")
    unittest.main()
    