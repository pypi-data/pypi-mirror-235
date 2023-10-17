
<h1 align="center">
  <a href="https://reactnative.dev/">
	  thetennisplay
  </a>
</h1>

<p align="center">
  <strong>더 이상 자리 없어서 🎾 못치는 경우는 그만</strong><br>
</p>

thetennisplay은 [thetennisplay](https://www.thetennisplay.com) (테니스 예약 사이트)에서 자리가 났을 때 알려주는 프로그램 입니다

## Contents

- [How to install](#-how-to-install)
- [Documentation](#-documentation)
- [How to Contribute](#-how-to-contribute)
- [Code of Conduct](#code-of-conduct)
- [License](#-license)


## 📋 How to Install

** `Chrome`, `Chromedriver` 설치를 요구합니다!**

### Method 1 (PyPI)
`pip install thetennisplay`
`python -m thetennisplay`

### Method 2 (직접 Build하기)
`git clone https://github.com/jaycho1214/thetennisplay`
`pip install .`
`python -m thetennisplay`


## 📖 Documentation

`thetennisplay watch [OPTIONS]`

### 계정 (필수)
`--username 이메일`
`--password 비밀번호`
[thetennisplay](https://www.thetennisplay.com)에 로그인할 때 사용되는 계정입니다. 계정은 로그인 할때만 사용되며 어떠한 형태로도 저장되지 않습니다 :)

**카카오 로그인은 현재 지원하지 않습니다**


### 예약 정보
`--court [코트]`
예약할려는 코트를 입력합니다

**현재 예약 가능 코트**
* `반포종합운동장 테니스장`
* `동작주차공원 테니스장`

`--date [날짜 (YYYY-MM-DD)]`
예약할려는 날짜를 년-월-일 (예: 2023-10-16)로 입력하면 이때 비어있는 코트를 확인합니다
`--hour [시간]`
예약할려는 시간을 `14`또는 `14-18`와 같이 입력하면 이때 시간이 나는 경우 소리로 알려줍니다. 위 값이 없을경우 그 시간대에 아무 시간이나 자리가 있으면 알려줍니다

## 👏 How to Contribute

발견된 문제나 피드백은 여기로 알려주세요 :)
[제보하기](https://github.com/jaycho1214/thetennisplay/issues)

## 📄 License

[MIT License]
(https://github.com/jaycho1214/thetennisplay/blob/main/LICENSE)