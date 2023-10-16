create table class (
	id text(50) not null primary key,
	name text(255) not null,
	source text(50) not null,
	role_prompt text,
	type text(50) not null,
	create_time integer,
	update_time integer,
	order_id integer,
	user_id text
);

create table prompt  (
	id text(50) not null primary key,
	name text(255) not null,
	note text,
	prompt text,
	source text(50) not null,
	role_id text(50),
	scene_id text(50),
	labels_ids text,
	variables text,
	collecte_status text(50),
	create_time integer,
	update_time integer,
	user_id text
);

create table model  (
	id text(50) not null primary key,
	name text(255) not null,
	description text,
	config text not null,
	params text not null,
	source text(50) not null,
	enable_stream integer,
	is_default integer,
	create_time integer,
	update_time integer,
	user_id text
);

create table module  (
	id text(50) not null primary key,
	name text(255) not null,
	description text,
	source text(50) not null,
	type text(50) not null,
	"group" text(50) not null,
	params text not null,
	inputs text not null,
	outputs text not null,
	create_time integer,
	update_time integer,
	user_id text
);

insert into module (id, name, description, "source", "type","group", params, inputs, outputs, create_time, update_time, user_id)
values
('00000000-0000-0000-0000-000000000001', 'input', 'input', 'system', 'input','input', '[]', '[]', '[{"name":"assignment","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
('00000000-0000-0000-0000-000000000002', 'output', 'output', 'system', 'output', 'output','[]', '[{"name":"result1","type":"any","defaultvalue":null,"value":null}]', '[]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),

('00000000-0000-0000-aaaa-000000000001', 'define prompt', 'define prompt', 'system', 'prompt','prompt', '[]', '[]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
('00000000-0000-0000-aaaa-000000000002', 'chat message prompt template', 'ChatMessagePromptTemplate', 'system', 'script_prompt','prompt', '[]', '[]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
('00000000-0000-0000-aaaa-000000000003', 'chat prompt template', 'ChatPomptTemplate', 'system', 'script_prompt','prompt', '[]', '[]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
('00000000-0000-0000-aaaa-000000000004', 'human message prompt template', 'HumanMessagePromptTempalte', 'system', 'script_prompt','prompt', '[]', '[]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
('00000000-0000-0000-aaaa-000000000005', 'prompt template', 'PromptTemplate', 'system', 'script_prompt','prompt', '[]', '[]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
('00000000-0000-0000-aaaa-000000000006', 'system message prompt template', 'SystemMessagePromptTemplate', 'system', 'script_prompt','prompt', '[]', '[]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),

('00000000-0000-0000-1111-000000000001', 'python3 script', 'python3 script', 'system','script', 'tool', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"true"}]', '[{"name":"input","type":"any","defaultvalue":"","value":null,"description":""}]', '[{"name":"output","type":"any","defaultvalue":"","value":null,"description":""}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
('00000000-0000-0000-bbbb-000000000001', 'text segmentation', 'text segmentation', 'system','script', 'tool', '[{"name":"script","type":"script","default_value":"","value":"","editable":"false"},{"name":"chunk_size","type":"int","default_value":"","value":""},{"name":"chunk_overlap","type":"int","default_value":"","value":""},{"name":"separators","type":"text","default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":"","value":null,"description":""}]', '[{"name":"output","type":"any","defaultvalue":"","value":null,"description":""}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
('00000000-0000-0000-bbbb-000000000002', 'text truncation', 'text truncation', 'system','script', 'tool', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"max_length","type":"int","default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":"","value":null,"description":""}]', '[{"name":"output","type":"any","defaultvalue":"","value":null,"description":""}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),

('00000000-0000-0000-cccc-000000000001', 'chroma writer', 'chroma writer', 'system', 'vectordb','vectordb', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"connection_type","type":"select","options":[],"default_value":"local;remote","value":""},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"collection","type":"text","options":[],"default_value":"","value":""},{"name":"n_results","type":"int","options":[],"default_value":"10","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
('00000000-0000-0000-cccc-000000000002', 'chroma reader', 'chroma reader', 'system', 'vectordb','vectordb', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"collection","type":"text","options":[],"default_value":"","value":""},{"name":"n_results","type":"int","options":[],"default_value":"10","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
('00000000-0000-0000-cccc-000000000003', 'dingodb writer', 'dingodb writer', 'system', 'vectordb','vectordb', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"connection_type","type":"select","options":[],"default_value":"local;remote","value":""},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"index","type":"text","options":[],"default_value":"","value":""},{"name":"user","type":"text","options":[],"default_value":"","value":""},{"name":"password","type":"text","options":[],"default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
('00000000-0000-0000-cccc-000000000004', 'dingodb reader', 'dingodb reader', 'system', 'vectordb','vectordb', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"index","type":"text","options":[],"default_value":"","value":""},{"name":"user","type":"text","options":[],"default_value":"","value":""},{"name":"password","type":"text","options":[],"default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001');





--insert into module (id, name, description, "source", "type","group", params, inputs, outputs, create_time, update_time, user_id)
--values
--('00000000-0000-0000-0000-000000000001', 'input', 'input', 'system', 'input','input', '[]', '[]', '[{"name":"assignment","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-0000-000000000002', 'output', 'output', 'system', 'output', 'output','[]', '[{"name":"result1","type":"any","defaultvalue":null,"value":null}]', '[]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--
--('00000000-0000-0000-aaaa-000000000001', 'define prompt', 'define prompt', 'system', 'prompt','prompt', '[]', '[]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-aaaa-000000000002', 'chatmessageprompttemplate', 'chatmessageprompttemplate', 'system', 'prompt','prompt', '[]', '[]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-aaaa-000000000003', 'chatprompttemplate', 'chatprompttemplate', 'system', 'prompt','prompt', '[]', '[]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-aaaa-000000000004', 'humanmessageprompttemplate', 'humanmessageprompttemplate', 'system', 'prompt','prompt', '[]', '[]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-aaaa-000000000005', 'prompttemplate', 'prompttemplate', 'system', 'prompt','prompt', '[]', '[]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-aaaa-000000000006', 'systemmessageprompttemplate', 'systemmessageprompttemplate', 'system', 'prompt','prompt', '[]', '[]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--
--('00000000-0000-0000-1111-000000000001', 'python3 script', 'python3 script', 'system','script', 'tool', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"true"}]', '[{"name":"input","type":"any","defaultvalue":"","value":null,"description":""}]', '[{"name":"output","type":"any","defaultvalue":"","value":null,"description":""}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-bbbb-000000000001', 'text segmentation', 'text segmentation', 'system','script', 'tool', '[{"name":"script","type":"script","default_value":"","value":"","editable":"false"},{"name":"chunk_size","type":"int","default_value":"","value":""},{"name":"chunk_overlap","type":"int","default_value":"","value":""},{"name":"separators","type":"text","default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":"","value":null,"description":""}]', '[{"name":"output","type":"any","defaultvalue":"","value":null,"description":""}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-bbbb-000000000002', 'text truncation', 'text truncation', 'system','script', 'tool', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"max_length","type":"int","default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":"","value":null,"description":""}]', '[{"name":"output","type":"any","defaultvalue":"","value":null,"description":""}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-bbbb-000000000003', 'character textspliter', 'character textspliter', 'system','script', 'tool', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"true"}]', '[{"name":"input","type":"any","defaultvalue":"","value":null,"description":""}]', '[{"name":"output","type":"any","defaultvalue":"","value":null,"description":""}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-bbbb-000000000004', 'recursive character text', 'recursive character text', 'system','script', 'tool', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"true"}]', '[{"name":"input","type":"any","defaultvalue":"","value":null,"description":""}]', '[{"name":"output","type":"any","defaultvalue":"","value":null,"description":""}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--
--('00000000-0000-0000-cccc-000000000002', 'chroma reader', 'chroma reader', 'system', 'vectordb','vectordb', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"collection","type":"text","options":[],"default_value":"","value":""},{"name":"n_results","type":"int","options":[],"default_value":"10","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-cccc-000000000003', 'faiss reader', 'faiss reader', 'system', 'vectordb','vectordb', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"collection","type":"text","options":[],"default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-cccc-000000000004', 'dingodb reader', 'dingodb reader', 'system', 'vectordb','vectordb', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"index","type":"text","options":[],"default_value":"","value":""},{"name":"user","type":"text","options":[],"default_value":"","value":""},{"name":"password","type":"text","options":[],"default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-cccc-000000000005', 'chroma writer', 'chroma writer', 'system', 'vectordb','vectordb', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"connection_type","type":"select","options":[],"default_value":"local;remote","value":""},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"collection","type":"text","options":[],"default_value":"","value":""},{"name":"n_results","type":"int","options":[],"default_value":"10","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-cccc-000000000006', 'faiss writer', 'faiss writer', 'system', 'vectordb','vectordb', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"collection","type":"text","options":[],"default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-cccc-000000000007', 'dingodb writer', 'dingodb writer', 'system', 'vectordb','vectordb', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"connection_type","type":"select","options":[],"default_value":"local;remote","value":""},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"index","type":"text","options":[],"default_value":"","value":""},{"name":"user","type":"text","options":[],"default_value":"","value":""},{"name":"password","type":"text","options":[],"default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-cccc-000000000008', 'multiqueryretriever', 'multiqueryretriever', 'system', 'vectordb','vectordb', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"index","type":"text","options":[],"default_value":"","value":""},{"name":"user","type":"text","options":[],"default_value":"","value":""},{"name":"password","type":"text","options":[],"default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--
--('00000000-0000-0000-dddd-000000000001', 'agentintitalzer', 'agentintitalzer', 'system', 'agent','agent', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"collection","type":"text","options":[],"default_value":"","value":""},{"name":"n_results","type":"int","options":[],"default_value":"10","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-dddd-000000000002', 'csvagent', 'csvagent', 'system', 'agent','agent', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"collection","type":"text","options":[],"default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-dddd-000000000003', 'jsonagent', 'jsonagent', 'system', 'agent','agent', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"index","type":"text","options":[],"default_value":"","value":""},{"name":"user","type":"text","options":[],"default_value":"","value":""},{"name":"password","type":"text","options":[],"default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-dddd-000000000004', 'openai conversationl', 'openai conversationl', 'system', 'agent','agent', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"index","type":"text","options":[],"default_value":"","value":""},{"name":"user","type":"text","options":[],"default_value":"","value":""},{"name":"password","type":"text","options":[],"default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-dddd-000000000005', 'vectorstoreagent', 'vectorstoreagent', 'system', 'agent','agent', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"index","type":"text","options":[],"default_value":"","value":""},{"name":"user","type":"text","options":[],"default_value":"","value":""},{"name":"password","type":"text","options":[],"default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-dddd-000000000006', 'zeroshotagent', 'zeroshotagent', 'system', 'agent','agent', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"index","type":"text","options":[],"default_value":"","value":""},{"name":"user","type":"text","options":[],"default_value":"","value":""},{"name":"password","type":"text","options":[],"default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--
--('00000000-0000-0000-eeee-000000000001', 'csvloader', 'csvloader', 'system', 'loader','loader', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"collection","type":"text","options":[],"default_value":"","value":""},{"name":"n_results","type":"int","options":[],"default_value":"10","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-eeee-000000000002', 'textloader', 'textloader', 'system', 'loader','loader', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"collection","type":"text","options":[],"default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--
--('00000000-0000-0000-ffff-000000000001', 'cohereembeddings', 'cohereembeddings', 'system', 'embedding','embedding', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"collection","type":"text","options":[],"default_value":"","value":""},{"name":"n_results","type":"int","options":[],"default_value":"10","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-ffff-000000000002', 'huggingfaceembeddings', 'huggingfaceembeddings', 'system', 'embedding','embedding', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"collection","type":"text","options":[],"default_value":"","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--('00000000-0000-0000-ffff-000000000003', 'openaiembeddings', 'openaiembeddings', 'system', 'embedding','embedding', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"collection","type":"text","options":[],"default_value":"","value":""},{"name":"n_results","type":"int","options":[],"default_value":"10","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001'),
--
--('00000000-0000-0000-1111-000000000002', 'prompt runner', 'prompt runner', 'system', 'chains','chains', '[{"name":"script","type":"script","options":[],"default_value":"","value":"","editable":"false"},{"name":"host","type":"text","options":[],"default_value":"","value":""},{"name":"port","type":"text","options":[],"default_value":"","value":""},{"name":"collection","type":"text","options":[],"default_value":"","value":""},{"name":"n_results","type":"int","options":[],"default_value":"10","value":""}]', '[{"name":"input","type":"any","defaultvalue":null,"value":null}]', '[{"name":"output","type":"any","defaultvalue":null,"value":null}]', 1691978400, 1691978400, '00000000-1111-0000-000a-000000000001');
--

create table flow  (
	id text(50) not null primary key,
	name text(255) not null,
	description text,
	config text not null,
	model_ids text,
	params text not null,
	source text(50) not null,
	prompt_count integer,
	create_time integer,
	update_time integer,
	user_id text
);

create table app  (
	id text(50) not null primary key,
	name text(255) not null,
	description text,
	flow_id id text(50),
	input_info text,
	source text(50) not null,
	create_time integer,
	update_time integer,
	user_id text
);

insert into class
(id, name, "source", role_prompt, "type", create_time, update_time, order_id, user_id)
values('00000000-0000-0000-0000-000000000001', 'others', 'system', 'preset scene ','scene', 1691978400,1691978400, 2147483647, '00000000-1111-0000-000a-000000000001');
insert into class
(id, name, "source", role_prompt, "type", create_time, update_time, order_id, user_id)
values('00000000-0000-0000-0000-000000000002', 'none', 'system', 'preset role ','role', 1691978400,1691978400, 1, '00000000-1111-0000-000a-000000000001');
