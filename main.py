try:
   import base64,marshal,os,click
   from uncompyle6 import main
except ImportError:
   os.system("pip3 install click uncompyle6 &> /dev/null")
class Com:
        def __init__(self,fil,jum):
                self.file=fil
                self.cout=0
                self.jml=jum
                self.mars(open(fil,'r').read())

        def mars(self,strg):
                x=compile(strg,'<script>','exec')
                xx=marshal.dumps(x)
                xxx=f"#Compiled By Aslanz\n#https://youtube.com/aslanz\n\nimp>
                if self.cout == self.jml:
                        with open(self.file.replace('.py','_comlap.py'),'w') >
                                com.write(xxx)
                        print(f"\033[1;32m[+] \033[1;37mSuccessfully seved as>
                        return True
                self.bes(xxx)

        def bes(self,strg):
                en=base64.b64encode(bytes(strg,'utf-8'))
                de=f"#Compiled By Aslanz\n#https://youtube.com/aslanz\nimport>
                self.cout+=1
                self.mars(de)

try:
        ofile=input("\033[1;33m[+] \033[1;37mScript > \033[1;32m")
        juml=int(input("\033[1;33m[+] \033[1;37mCount > \033[1;32m"))
        if juml > 100:
                click.pause("\033[1;31m[!] Warning Script error")
        Com(ofile,juml)
        pil=input("\033[1;33m[+] \033[1;37mCompile bytes code (y/n) > \033[1;>
        if pil.lower() == 'y':
                main.compile_file(ofile.replace('.py','_enc.py'))
                print("\033[1;32m[+] \033[1;37mDone")
        else:
                print("\033[1;32m[+] \033[1;37mDone")
except KeyboardInterrupt:
        exit()
except Exception as F:
        exit()
