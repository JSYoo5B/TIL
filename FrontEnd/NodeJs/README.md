# Node.js for front-end development
이전에 Front-end 개발자들도 node.js를 사용한다는 글을 본 적이 있다. 분명
node.js는 javascript를 서버 개발에(back-end) 사용하는 것이 가장 큰 특징인데 그
과정에서 node.js 기능들을 패키지로 모듈화 해서 쉽게 라이브러리를 가져다 쓰게
하려고 npm이 개발된 것으로 알고 있다. Front-end 개발자들이 npm, yarn, webpack
등을 이용하여 front-end용 패키지 관리 & 빌드 등에 활용하는 것으로 보인다.

## nvm으로 Node.js 버전 변경하기
해당 프로젝트가 특정 버전을 요구하는 경우 (설치된 버전이 낮거나, 요구 버전이
다른 2개 프로젝트를 한 PC에서 작업해야 하는 경우)
[nvm](https://github.com/nvm-sh/nvm)으로 Noda.js의 버전 변경을 쉽게 할수 있다.

 1. nvm을 각 플랫폼에 맞게 설치한다.
     *  Ubuntu: nvm/README.md의 설명대로 curl이나 wget으로 설치
     *  macOS: `$ brew install nvm`
     *  ArchLinux: `$ yay -S nvm`
 2. nvm 활성화 명령을 startup script에 추가, 활성화 (bashrc, zshrc등)  
    zsh에서 Ubuntu, macOS, ArchLinux 모두 호환되도록 작성한 startup script는
    [ConfigFiles](https://github.com/JSYoo5B/ConfigFiles/blob/180c900/linux/zsh/.zsh_devconfig#L14-L33)
    참고
 3. 기존 node에서 npm으로 global하게 설치한 모듈이 확인되면 경고를 출력한다.  
    기존 설치된 node를 system이라 함.  
    설명에 따라 npm으로 충돌이 우려되는 npm package를 제거한다.
 4. `$ nvm install <VERSION>`으로 원하는 node 버전을 설치한다.
 5. `$ nvm use <VERSION>`으로 설치된 node 버전 중 특정 버전으로 변경 가능하다.
 6. `$ node --version` 및 `$ npm --version` 으로 사용중인 node 및 npm 버전 확인
