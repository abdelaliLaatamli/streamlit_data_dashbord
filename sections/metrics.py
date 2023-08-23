def set_metrics(st,data):
    if not data.empty :
        c1,c2,c3,c4,c5=st.columns(5)
        with c1:
            st.info('Queued', icon="📤")
            st.metric(label='Message', value=f"{data['total_count'].sum():,}")
        with c2:
            st.info('Delivered', icon="🚚")
            st.metric(label='Message', value=f"{data[data['type'] == 'delivered']['total_count'].sum():,}")
        with c3:
            st.info('Bounce', icon="⛔")
            st.metric(label='Message', value=f"{data[data['type'] == 'bounce']['total_count'].sum():,}")
        with c4:
            st.info('Soft Bounce', icon="⚠")
            st.metric(label='Message', value=f"{data[(data['type'] == 'bounce') & (data['bounce_type'] == 'soft')]['total_count'].sum():,}")
        with c5:
            st.info('Hard Bounce', icon="🚫")
            st.metric(label='Message', value=f"{data[(data['type'] == 'bounce') & (data['bounce_type'] == 'hard')]['total_count'].sum():,}")