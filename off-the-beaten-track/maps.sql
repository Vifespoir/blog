# postid-id
SELECT post_id, meta_value FROM wordpress.wp2_postmeta
	WHERE meta_key = '_wp_attached_file';
# postid-ppath + filtering to keep only jpg entries
SELECT post_parent, guid FROM wordpress.wp2_posts WHERE post_parent > 0;
# pid-gid
SELECT pid, galleryid FROM wordpress.wp2_ngg_pictures;
# pid-name
SELECT pid, filename FROM wordpress.wp2_ngg_pictures;
# gid-path
SELECT gid, path FROM wordpress.wp2_ngg_gallery;
