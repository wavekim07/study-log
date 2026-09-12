## React가 뭔가
웹 화면(UI)을 만드는 JavaScript 라이브러리. 화면을 작은 조각(컴포넌트)으로 나눠서 조립하는 방식.

## 핵심 용어
- **Node.js**: JavaScript를 브라우저 밖(컴퓨터)에서 실행할 수 있게 해주는 프로그램. 리액트 개발의 기반.
- **npm**: Node.js용 패키지 관리자. 남이 만든 라이브러리를 설치/관리 (Python의 pip 같은 역할).
- **npx**: 설치 없이 도구를 일회성으로 실행. 새 프로젝트 만들 때 주로 사용.
- **Vite**: 리액트 프로젝트를 빠르게 생성/실행해주는 빌드 도구. `npm create vite@latest` 명령으로 새 프로젝트 시작.
- **JSX**: HTML처럼 생겼지만 JavaScript 안에 화면 구조를 쓸 수 있게 해주는 문법. `.jsx` 확장자.
- **컴포넌트(Component)**: 화면의 한 조각(예: 버튼, 카드, 헤더)을 함수 하나로 표현한 것.

## 프로젝트 실행 흐름 (Vite 기준)
1. `npm create vite@latest 프로젝트명` → 새 프로젝트 생성
2. `cd 프로젝트명` → 폴더 이동
3. `npm install` → 필요한 라이브러리 설치 (node_modules 생성)
4. `npm run dev` → 개발 서버 실행, 브라우저에서 확인

## 헷갈렸던 점
- Vite와 Eclipse는 무관함 (Vite=리액트/VS Code, Eclipse=JSP)