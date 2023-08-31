def set_metrics(st,data_logs , data_actions):
    if not data_logs.empty :
        c1,c2,c3,c4,c5=st.columns(5)
        with c1:
            st.info('Queued', icon="📤")
            st.metric(label='Message', value=f"{data_logs['total_count'].sum():,}")
        with c2:
            st.info('Delivered', icon="🚚")
            st.metric(label='Message', value=f"{data_logs[data_logs['type'] == 'delivered']['total_count'].sum():,}")
        with c3:
            st.info('Bounce', icon="⛔")
            st.metric(label='Message', value=f"{data_logs[data_logs['type'] == 'bounce']['total_count'].sum():,}")
        with c4:
            st.info('Soft Bounce', icon="⚠")
            st.metric(label='Message', value=f"{data_logs[(data_logs['type'] == 'bounce') & (data_logs['bounce_type'] == 'soft')]['total_count'].sum():,}")
        with c5:
            st.info('Hard Bounce', icon="🚫")
            st.metric(label='Message', value=f"{data_logs[(data_logs['type'] == 'bounce') & (data_logs['bounce_type'] == 'hard')]['total_count'].sum():,}")


    if not data_actions.empty :
        c1,c2,c3,c4,c5=st.columns(5)
        with c1:
            st.info('Requests', icon="🔛")
            st.metric(label='Request', value=f"{data_actions['total_count'].sum():,}")
        with c2:
            st.info('Open', icon="📖")
            st.metric(label='Message', value=f"{data_actions[data_actions['type'] == 'open']['total_count'].sum():,}")
        with c3:
            st.info('Click', icon="👆")
            st.metric(label='Message', value=f"{data_actions[data_actions['type'] == 'click']['total_count'].sum():,}")
        with c4:
            st.info('Unsub', icon="⚠")
            st.metric(label='Message', value=f"{data_actions[(data_actions['type'] == 'unsub') & (data_logs['bounce_type'] == 'soft')]['total_count'].sum():,}")
        with c5:
            st.info('Conversion', icon="🚫")
            st.metric(label='Message', value=f"{data_actions[data_actions['type'] == 'oops']['total_count'].sum():,}")