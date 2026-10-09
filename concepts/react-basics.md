## 큰 그림 (계층 구조)
Node.js  → JavaScript를 브라우저 없이 실행 가능하게 하는 기반 환경
Vite     → 리액트 프로젝트 뼈대 생성 + 개발 서버 실행 도구
React    → 화면(UI)을 만드는 JavaScript 라이브러리 (프론트엔드 전용)
JSX      → React를 사용할 때, 화면 구조를 코드 안에 표현하는 문법

## JavaScript와 Node.js
- JavaScript는 원래 브라우저 안에서 화면을 동작시키는(프론트엔드) 용도로 탄생한 언어. Java와는 이름만 비슷할 뿐 별개의 언어.
- Node.js는 브라우저 없이 컴퓨터에서 독립적으로 JavaScript를 실행할 수 있게 해주는 프로그램. 이 덕분에 JavaScript로 서버(백엔드) 개발도 가능해짐.

## React가 뭔가
웹 화면(UI)을 만드는 JavaScript 라이브러리. 화면을 작은 조각(컴포넌트)으로 나눠서 조립하는 방식.

## 핵심 용어
- **Node.js**: JavaScript를 브라우저 밖(컴퓨터)에서 실행할 수 있게 해주는 프로그램. 리액트 개발의 기반.
- **npm**: Node.js용 패키지 관리자. 남이 만든 라이브러리를 설치/관리 (Python의 pip 같은 역할).
- **npx**: 설치 없이 도구를 일회성으로 실행. 새 프로젝트 만들 때 주로 사용.
- **Vite**: 리액트 프로젝트를 빠르게 생성/실행해주는 빌드 도구. `npm create vite@latest` 명령으로 새 프로젝트 시작.
- **JSX**: React를 사용할 때, JavaScript 코드 안에서 `<h1></h1>` 같은 HTML 스타일 태그를 그대로 쓸 수 있게 해주는 문법. `.jsx` 확장자. 브라우저는 JSX를 직접 이해하지 못하므로, Vite가 순수 JavaScript로 변환(트랜스파일)해줌.
- **컴포넌트(Component)**: 화면의 한 조각(예: 버튼, 카드, 헤더)을 함수 하나로 표현한 것.

## State (useState)
- `const [값, set값함수] = useState(초기값)` 형태로 사용
- 일반 변수와 달리, state가 바뀌면 화면이 자동으로 다시 그려짐 (리렌더링)
- state는 props로 자식 컴포넌트에 전달 가능 (값과 변경 함수 둘 다)

## state 업데이트 시 주의점
- 같은 렌더링 안에서 setState를 여러 번 연속 호출할 때, `setX(x + 1)` 형태는 누적되지 않음 (매번 같은 이전 값을 참조)
- `setX(prev => prev + 1)` 형태를 쓰면 이전 값을 기준으로 정확히 누적됨

## 배열/객체 State와 불변성
- state가 배열/객체일 때, 원본을 직접 수정(push, 필드 직접 대입 등)하면 리액트가 변화를 감지 못해 화면이 갱신되지 않을 수 있음
- 항상 스프레드 연산자(`...`)로 기존 내용을 복사한 "새로운 배열/객체"를 만들어 교체해야 함
  - 배열에 추가: `setArr(prev => [...prev, 새값])`
  - 배열 항목 일부 수정: `setArr(prev => prev.map(item => 조건 ? {...item, 필드: 새값} : item))`
  - 배열 항목 삭제: `setArr(prev => prev.filter(item => 조건))`
  - 객체 필드 수정: `setObj(prev => ({...prev, 필드: 새값}))`

## 동적 필드명 (computed property name)
- `{ [변수]: 값 }` 형태로, 변수의 값을 객체의 키 이름으로 사용 가능
- 하나의 함수로 여러 필드를 처리할 때 유용 (예: `updateUser(field, value)`)

## useEffect와 부수효과(side effect)
- 부수효과: 화면 그리기 외의 작업(데이터 요청, 타이머, 로그 등). 렌더링 중에 직접 실행하지 않고 `useEffect` 안에서 처리
- 렌더링 중에 setState를 직접 호출하면 상태 변경 → 렌더링 → setState가 무한 반복됨
- 의존성 배열에 따라 실행 시점이 달라짐
  - `[]`: 마운트 시 1번
  - `[x]`: 마운트 시 + x가 바뀔 때마다
  - 생략: 매 렌더링 후
- 클린업 함수(`return () => {...}`): 컴포넌트가 사라질 때, 다음 effect 실행 직전에 실행 (타이머 정리, 이전 요청 결과 무시 등)

## fetch로 비동기 데이터 가져오기
- 상태 3개로 관리: 데이터 / loading(Pending) / error(Rejected)
- `async/await` + `try/catch/finally` (성공·실패와 무관하게 finally에서 loading 해제)
- fetch는 404/500에서도 reject하지 않으므로 `response.ok`를 확인하고 직접 throw
- `useEffect` 콜백에는 async를 직접 붙일 수 없어서, 안에 async 함수를 정의하고 호출
- `isCancelled` 플래그: 요청 자체를 취소하는 것이 아니라, 늦게 도착한 결과가 상태를 덮어쓰지 않게 무시하는 패턴 (진짜 취소는 AbortController)

## 디바운스 (입력 검색)
- 입력할 때마다 요청하지 않고, 입력이 멈춘 뒤 일정 시간(500ms) 후 1번만 요청
- `setTimeout`으로 예약하고, 클린업에서 `clearTimeout`으로 이전 예약을 취소

## 리렌더링 최적화 (memo / useCallback / useMemo)
- 기본 동작: 부모가 리렌더링되면 props가 그대로여도 자식 컴포넌트도 모두 리렌더링됨
- `memo(컴포넌트)`: props가 이전과 같으면(얕은 비교) 리렌더링을 건너뜀
- 함수는 렌더링마다 새로 만들어져 주소가 바뀌므로, 함수를 props로 넘기면 memo가 무력화됨 → `useCallback(함수, [의존성])`으로 함수 주소를 유지
- `useMemo(() => 계산, [의존성])`: 의존성이 안 바뀌면 이전 계산 결과를 재사용 (useCallback은 함수 캐싱, useMemo는 값 캐싱)
- `useCallback(..., [])` 안에서는 `setCount(prev => prev + 1)`처럼 함수형 업데이트를 써야 낡은 값 문제 없이 의존성 `[]`로 안전하게 쓸 수 있음
- 불변성과 연결: `[...prev, newTodo]`는 기존 항목의 참조를 유지하므로, 새 항목을 추가해도 기존 항목 컴포넌트(memo)는 다시 그려지지 않음
- 최적화 도구이므로 작은 앱에서는 필수가 아님 (console.log로 효과를 확인하며 사용)

## 폼 제출과 preventDefault
- `<form onSubmit={handleSubmit}>`에서 `e.preventDefault()`로 브라우저의 기본 제출 동작(페이지 이동/새로고침)을 막고 리액트에서 직접 처리
- form 안의 `<button>`은 type을 생략하면 제출 버튼으로 동작 (Enter로도 제출됨)

## 외부 라이브러리 설치 (lucide-react)
- 프로젝트 폴더에서 `npm install 패키지명`으로 설치하면 `package.json`에 기록됨
- `node_modules`는 `.gitignore`로 제외되므로, 저장소를 새로 받았을 때는 `npm install`로 다시 설치
- lucide-react: 아이콘을 컴포넌트로 가져와 `<Trash2 size={20} />`처럼 사용

## 이벤트 핸들러 작성 시
- `onChange={(e) => handleFunc(e)}` 처럼 이벤트 객체(e)를 매개변수로 명시하는 것이 안전 (전역 event 객체 직접 참조는 지양)

## 개발 서버란
`npm run dev`로 실행되는 서버는 "내 컴퓨터 안에서만 도는 임시 미리보기 서버"이지, 여러 사람이 접속하는 진짜 서비스 서버가 아님. 진짜 서비스를 위해선 별도로 서버(데이터베이스, 보안 포함)를 구축해야 함.

## 프로젝트 실행 흐름 (Vite 기준)
1. `npm create vite@latest 프로젝트명` → 새 프로젝트 생성
2. `cd 프로젝트명` → 폴더 이동
3. `npm install` → 필요한 라이브러리 설치 (node_modules 생성)
4. `npm run dev` → 개발 서버 실행, 브라우저에서 확인

## 헷갈렸던 점
- Vite와 Eclipse는 무관함 (Vite=리액트/VS Code, Eclipse=JSP)
- JSX는 "개발 환경"이 아니라 React를 쓸 때의 "문법"일 뿐임
- React는 기본적으로 프론트엔드 전용 (백엔드는 별도 도구 필요)
- fetch는 404/500 응답에서도 catch로 가지 않음 → `response.ok` 확인 필요
- `isCancelled`는 요청을 취소하는 게 아니라 결과를 무시하는 것
- `[]` 의존성의 effect 안에서 state를 갱신할 때는 `prev =>` 패턴이 안전 (StrictMode 개발 모드에서는 effect가 2번 실행되어 값이 중복될 수 있음)
- 검색어처럼 사용자 입력을 URL에 넣을 때는 `encodeURIComponent`로 감싸기
- `useCallback(..., [])` 안에서 state를 직접 읽으면 처음 값에 고정됨(stale closure) → `prev =>` 함수형 업데이트 사용 (MemoBasic에서 count가 1에서 멈춘 사례)
- memo는 "props가 같을 때만" 건너뜀 → `label={text}`처럼 바뀌는 props를 넘기면 그때마다 리렌더링됨
- useMemo는 의존성과 무관한 이유로 리렌더링될 때 효과가 보임 (MemoValue는 data 변경으로만 리렌더링되어 효과가 안 보임)
- checked만 있고 onChange가 없는 체크박스는 토글이 안 되고 경고가 뜸