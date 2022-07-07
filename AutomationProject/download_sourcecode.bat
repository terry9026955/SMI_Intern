set JENKINS_WORKSPACE=D:\Tinghao.Chen\Desktop\oneTouch_tool\auto_log
set GERRIT_PROJECT=SM2269
If %GERRIT_PROJECT% EQU SM2269 ( set GERRIT_PROJECT=SM2269XT_EchoHarbor)

echo %GERRIT_PROJECT%
echo %GERRIT_BRANCH%

set GERRIT_USER_ACCOUNT=ts.tsai
set GERRIT_HOST=rd2gerrit01.siliconmotion.com.tw

echo errorlevel = %errorlevel% >> %JENKINS_WORKSPACE%\Debug.log

echo "========== Download Source Code ==========" >> %JENKINS_WORKSPACE%\Debug.log

set JENKINS_SOURCECODE_PATH=D:\SourceCode_SM%val%

::rmdir /s /q %JENKINS_SOURCECODE_PATH% >> %JENKINS_WORKSPACE%\Debug.log
If Not Exist %JENKINS_SOURCECODE_PATH% (
	git clone --progress --recursive --branch %GERRIT_BRANCH% -v "ssh://ts.tsai@rd2gerrit01.siliconmotion.com.tw:29418/%GERRIT_PROJECT%" %JENKINS_SOURCECODE_PATH% >> %JENKINS_WORKSPACE%\Debug.log
)

If "%2"=="" (
Set VarSHA=""
::
:: Please input a custom branch in %VarSHA
:: Set VarSHA="1ab92d54" (User-defined) or Set VarSHA="" (Default "")
::
) else ( Set VarSHA=%2 )

echo %VarSHA%

del %JENKINS_WORKSPACE%\SHA.log
d:
cd %JENKINS_SOURCECODE_PATH%

If %VarSHA%=="" (
	git fetch -p
	git clean -fd
	git reset --hard HEAD
	git checkout %GERRIT_BRANCH%
	git pull
	git log --oneline -1 >> %JENKINS_WORKSPACE%\SHA.log
) else ( 
	git fetch -p
	git clean -fd
	git reset --hard HEAD
	git checkout %GERRIT_BRANCH%
	git checkout %VarSHA%
	git pull
	git log --oneline -1 >> %JENKINS_WORKSPACE%\SHA.log )

echo errorlevel = %errorlevel% >> %JENKINS_WORKSPACE%\Debug.log
pause