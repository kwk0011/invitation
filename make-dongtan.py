#!/usr/bin/env python3
"""index.html 에서 장소만 바꾼 dongtan.html 을 만듭니다.

돌잔치를 두 번 나눠 하기 때문에 초대장도 두 벌입니다.
  index.html    그룹 1 · 9월 24일(목) 17:30 · 강릉 씨마크 호텔
  dongtan.html  그룹 2 · 9월 12일(토) 11:00 · 화성 동탄 자택

사진, 돌잡이, 인사말 같은 나머지 내용은 전부 같습니다.
index.html 을 고친 뒤 이 스크립트를 다시 돌리면 그대로 옮겨집니다.

    python3 make-dongtan.py
"""
import io
import sys

SRC = "index.html"
DST = "dongtan.html"

# ── 카톡 미리보기 문구 (서버가 읽는 태그라 파일마다 따로 있어야 합니다) ──
OG_OLD = '<meta property="og:description" content="2026년 9월 24일 목요일 오후 5시 30분 · 씨마크 호텔 1층 더 레스토랑" />'
OG_NEW = '<meta property="og:description" content="2026년 9월 12일 토요일 오전 11시 · 화성 동탄 루나네 집" />'

# ── 날짜와 시간 (강릉과 다른 날에 따로 엽니다) ──
WHEN_OLD = """    at: "2026-09-24T17:30",                       // 잔치 일시 (D-day 계산용)
    whenText: "2026년 9월 24일 목요일 오후 5시 30분","""

WHEN_NEW = """    at: "2026-09-12T11:00",                       // 잔치 일시 (D-day 계산용)
    whenText: "2026년 9월 12일 토요일 오전 11시","""

# ── 장소 설정 ──
EVENT_OLD = '''    placeName: "씨마크 호텔 1층 더 레스토랑",
    address: "강원특별자치도 강릉시 해안로406번길 2",   // 화면에 표시되는 주소
    mapQuery: "강릉시 해안로406번길 2",                 // 지도 앱에서 검색할 말 (비우면 위 주소로 검색)
    notes: [
      "주차는 무료입니다.",
      "더 레스토랑은 호텔 1층에 있습니다.",
      "레스토랑 문의 033-650-7044"
    ]'''

EVENT_NEW = '''    placeName: "루나네 집",
    address: "경기도 화성시 동탄숲속로 69, 836동 1801호",   // 화면에 표시되는 주소
    mapQuery: "화성시 동탄숲속로 69",                       // 지도 앱에서 검색할 말 (동·호수는 빼야 검색됩니다)
    notes: [
      // 주차 방법, 공동현관 비밀번호 같은 안내를 여기에 적으세요.
      // 예) "지하 주차장으로 오시면 836동과 바로 이어집니다."
    ]'''

BANNER = """<!-- 이 파일은 make-dongtan.py 가 index.html 에서 만들어 냅니다.
     여기를 직접 고치면 다음에 스크립트를 돌릴 때 지워집니다.
     내용을 바꾸려면 index.html 을, 장소를 바꾸려면 make-dongtan.py 를 고치세요. -->
"""


def main() -> int:
    html = io.open(SRC, encoding="utf-8").read()

    for old, new, what in ((OG_OLD, OG_NEW, "카톡 미리보기 문구"),
                           (WHEN_OLD, WHEN_NEW, "날짜와 시간"),
                           (EVENT_OLD, EVENT_NEW, "장소 설정")):
        found = html.count(old)
        if found != 1:
            print(f"실패: {SRC} 안에서 {what}를 {found}군데 찾았습니다 (1군데여야 합니다).")
            print("index.html 의 해당 부분이 바뀌었다면 이 스크립트의 문자열도 맞춰 주세요.")
            return 1
        html = html.replace(old, new)

    # <!doctype html> 바로 다음 줄에 안내 문구를 끼웁니다
    line_end = html.index("\n") + 1
    html = html[:line_end] + BANNER + html[line_end:]

    io.open(DST, "w", encoding="utf-8").write(html)
    print(f"{DST} 를 만들었습니다. ({len(html):,}자)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
