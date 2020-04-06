# Vue.js 개발 시작하기
[Vue.js 퀵 스타트](http://www.yes24.com/Product/Goods/45091747)를 참고하여
공부하고 있음.

## Vue.js 개발환경 구축 (Vue-cli)
[nodejs 설치] -> [npm 설정] -> [yarn, @vue/cli 설치]
(이유는 FrontEnd/NodeJs 참고)

여기에서 문제가 생길 수 있는 부분은 설치된 node.js가 vue-cli 요구 버전보다
낮아서 @vue/cli의 `$ vue create`에서 실패하는 경우다. 대부분 문제는 ubuntu의
repo가 너무 구버전을 기본으로 하기 때문이다.
(기억으론 Ubuntu 18.04에서 제공되는 최신 nodejs 버전은 v8.10.0이다.)
해당 문제의 해결법은 FrontEnd/NodeJs의 NVM 부분을 참고.

## MVVM 패턴
Vue는 M-V-VM 패턴으로 구성되어있다. 정확한 연관관계대로 설명하자면 V-VM-M이다.
 *  View는 말 그대로 화면 구성 & GUI 출력을 담당한다.
 *  View-Model은 해당 view에서 data-binding과 command 처리, 알림을 전송한다.
 *  Model은 해당 제품에서 구현하고자 하는 대상(business logic)을 담당한다.

사실 이게 MVC나 MVVP나 MVVM이나 개념 자체는 GUI 입출력과 Business logic의
분리가 핵심 목표일텐데, 셋 다 뭔가 고만고만해서 차이를 잘 이해하기 힘들다.
해당 내용에 대해 더 공부할 필요가 있을 듯 하다.

# Vue.js 프로젝트 시작하기
```sh
vue create myapp
```
위와 같이 실행하면 myapp 폴더를 생성하고, 해당 폴더에 vuejs 개발에 필요한
패키지를 알아서 구성하고, git init + add + commit까지 진행해버린다. 일단 현재
보고있는 책에서는 unpkg.com에서 script를 불러오고, SPA 개발하는 방법을
설명하고 있으므로, 해당 내용을 따라 수행해보았다.

## GUI로 프로젝트 관리하기
```sh
vue ui
```
명령어 실행시 Vue 프로젝트 관리를 위한 웹 서버가 시작되고, 웹브라우저가
자동으로 실행된다. (원격 접속시 해당 서버의 GUI에서 웹브라우저가 자동 실행됨)

이 명령을 WSL에서 SSH로 접속해서 실행할 경우 문제가 생긴다. 원인은 vue-cli에서
웹 브라우저를 실행시키는 함수가 Windows 환경에서는 cmd.exe를 사용하는데 이걸
SSH 접속 상태에서 실행시키는 것이 불가능하다. (WSL Bash에서 실행하거나
[Windows Terminal](https://github.com/microsoft/terminal)로 실행하는 경우는
문제가 되지 않는다.) 웹브라우저 실행시키는 부분때문에 프로젝트 관리 웹 서버가
동작하지 않으므로 문제가 된다. 

`vue ui --headless` 명령으로 실행 시 웹브라우저 실행하는 부분만 방지한다. 
[(Code 참고)](https://github.com/vuejs/vue-cli/blob/0d0168b/packages/%40vue/cli/lib/ui.js#L77-L81)
이 외 관련 옵션은 `vue ui --help`로 확인하자