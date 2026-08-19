# 돌잔치 초대장

모바일에서 보기 좋은 한 페이지 초대장입니다. 빌드 도구 없이 `index.html` 하나로 동작합니다.

## 1. 내용 고치기

`index.html`을 열어 `▼▼▼ 여기만 고치면 됩니다 ▼▼▼` 아래의 `CONFIG` 부분만 바꾸면 됩니다.

| 항목 | 설명 |
| --- | --- |
| `baby` | 아이 이름, 부르는 이름, 태어난 날, 소개 항목(`facts`) |
| `parents` | 아빠·엄마 이름, 관계(첫째 딸 등) |
| `greeting` | 인사말. `\n`이 줄바꿈입니다 |
| `event` | 일시, 장소, 주소, 안내 사항(`notes`) |
| `contacts` | 전화 걸기 버튼 |
| `photos` | 사진 경로 목록 |
| `grabs` | 돌잡이 항목과 문구 |

`event.at`은 D-day 계산에만 쓰이므로 `2026-09-20T12:00` 형식을 지켜 주세요.

## 2. 사진 넣기

1. `images/` 폴더를 만들고 사진을 넣습니다.
2. `CONFIG.photos`에 경로를 적습니다. **첫 번째 사진이 맨 위 대표 사진**이 됩니다.

```js
photos: ["images/1.jpg", "images/2.jpg", "images/3.jpg"],
```

- 세로 사진(3:4, 4:5)이 가장 잘 맞습니다.
- 휴대폰 원본은 5MB가 넘어 느립니다. 가로 1200px 정도로 줄여서 올리세요.
- 비워 두면 "사진 자리" 표시가 나옵니다.

## 3. GitHub Pages로 올리기

```bash
git init
git add .
git commit -m "돌잔치 초대장"
git branch -M main
git remote add origin https://github.com/<아이디>/<저장소이름>.git
git push -u origin main
```

저장소 → **Settings → Pages → Source: Deploy from a branch → main / (root)** → Save.
1~2분 뒤 `https://<아이디>.github.io/<저장소이름>/` 으로 열립니다. 이 주소를 카톡으로 공유하면 됩니다.

> 저장소는 **Public**이어야 무료 계정에서 Pages가 켜집니다. `contacts`에 적은 전화번호는 링크를 아는 누구나 볼 수 있으니, 필요 없으면 `contacts: []` 로 비우세요.

## 4. 카톡 미리보기 문구

`index.html` 위쪽 `og:title`, `og:description`을 실제 내용으로 바꿔 주세요. 썸네일 이미지도 넣으려면 아래 줄을 추가합니다.

```html
<meta property="og:image" content="https://<아이디>.github.io/<저장소이름>/images/1.jpg" />
```

카톡은 미리보기를 캐시하므로, 바꾼 뒤에도 예전 내용이 보이면
[카카오 디버거](https://developers.kakao.com/tool/debugger/sharing)에서 캐시를 초기화하세요.

## 참고

- 다크 모드를 자동으로 따라갑니다.
- 돌잡이 선택은 방문자 브라우저에만 저장됩니다(집계 기능 없음).
- 축의금·계좌 안내는 넣지 않았습니다.
- 검색엔진 노출을 막는 `noindex` 태그가 들어 있습니다. 카톡 미리보기가 안 뜨면 `index.html` 상단의 해당 줄을 지우세요.
