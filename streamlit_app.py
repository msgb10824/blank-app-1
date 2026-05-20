\import streamlit as st

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="msgb cafe", page_icon="☕", layout="centered")
st.title('☕ msgb cafe 키오스크')
st.markdown('---')

# 2. 데이터 정의
menu = ['아메리카노', '카페라떼', '바닐라라떼', '딸기라떼']
price = [4000, 5000, 5500, 6000]

# 3. 메뉴판 보여주기 (깔끔하게 표 형태로 출력)
st.subheader("📋 메뉴판")
menu_data = {"메뉴": menu, "가격(원)": [f"{p:,}" for p in price]}
st.table(menu_data)

st.markdown('---')

# 4. 사용자 입력 받기
st.subheader("🛒 주문하기")

# 셀렉트박스를 사용하면 잘못된 번호를 입력하는 실수를 원천 차단할 수 있습니다!
selected_item = st.selectbox('메뉴를 선택해 주세요:', menu)
count = st.number_input('수량을 입력하세요:', min_value=1, max_value=20, value=1, step=1)

# 선택한 메뉴의 인덱스 찾기
idx = menu.index(selected_item)
total_price = count * price[idx]

st.markdown('---')

# 5. 결제 및 결과 출력
# 스트림릿의 버튼 컴포넌트 활용
if st.button('주문하기 (결제)', type='primary'):
    st.balloons() # 축하 효과 애니메이션 🎉
    
    # 결과 창을 이쁘게 띄워줍니다.
    st.success(f'✅ 주문이 완료되었습니다!')
    
    # 3열(Column) 레이아웃으로 영수증처럼 표현
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="선택하신 메뉴", value=selected_item)
    with col2:
        st.metric(label="수량", value=f"{count}잔")
    with col3:
        st.metric(label="총 결제금액", value=f"{total_price:,}원")
        
    st.info('msgb 카페를 이용해주셔서 감사합니다. 잠시만 기다려주세요! ☕')