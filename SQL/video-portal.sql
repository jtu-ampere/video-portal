-- public.videoplayer_video definition

-- Drop table
-- DROP TABLE public.videoplayer_video;

CREATE TABLE public.videoplayer_video (
	id int8 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE),
	title varchar(100) NOT NULL,
	mp4_file varchar(255) NOT NULL,
	vtt_file varchar(255) NOT NULL,
	gif_file varchar(255) NOT NULL,
	thumbnail_file varchar(255) NOT NULL,
	description text NOT NULL,
	CONSTRAINT videoplayer_video_pkey PRIMARY KEY (id)
);


-- public.videoplayer_videoprocess definition

-- Drop table
-- DROP TABLE public.videoplayer_videoprocess;

CREATE TABLE public.videoplayer_videoprocess (
	uuid uuid NOT NULL,
	title varchar(100) NOT NULL,
	description text NOT NULL,
	CONSTRAINT videoplayer_videoprocess_pkey PRIMARY KEY (uuid)
);