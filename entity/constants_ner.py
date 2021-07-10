map_order_entity = {}

# intent pattern matching
# tìm ngành
map_order_entity['major_name'] = ['point','subject_group','career','criteria','object','register','case']
map_order_entity['major_code']=['major_name','subject_group']
map_order_entity['point']=['major_name','subject_group','year','type_edu','case']
map_order_entity['subject_group']=['major_name','subject']
map_order_entity['subject']=['major_name','subject_group']
map_order_entity['tuition']=['type_edu']
map_order_entity['year'] = ['major_name','subject_group','point','subject']
map_order_entity['object'] = ['case','type_edu','major_name','register']
map_order_entity['register'] = ['case','type_edu','major_name','object']
map_order_entity['criteria'] = ['major_name','case','object','register','subject_group','subject','type_edu','year']
# intent deep learning
# label = ['other','type_edu','case','career']
map_order_entity['type_edu']=['major_name','subject_group','subject','case','object','register','criteria']
map_order_entity['case']=['major_name','criteria','subject','subject_group','case','register','criteria']
map_order_entity['career']=['major_name','subject','subject_group',"major_code"]

# map_order_entity['other']=['major_name','type_edu','point','year','career','subject','tuition','subject_group','case','major_code','criteria','object','register']



# bổ sung intent là INFORM cho user_request:
map_order_entity['not_intent']=['major_name','type_edu','point','year','career','subject','tuition','subject_group','case','major_code','criteria','object','register']
# print(len(map_order_entity['not_intent']))

map_order_entity['major_name_inform'] = ['major_name']
map_order_entity['major_code_inform'] = ['major_code']
map_order_entity['subject_group_inform'] = ['subject_group']
map_order_entity['point_inform'] = ['point']
map_order_entity['type_edu_inform'] = ['type_edu']
map_order_entity['year_inform'] = ['year']

map_order_entity['case_inform'] = ['case']
map_order_entity['criteria_inform'] = ['criteria']
map_order_entity['object_inform'] = ['object']
map_order_entity['register_inform'] = ['register']
map_order_entity['subject_inform'] = ['subject']
map_order_entity['career_inform'] = ['career']
map_order_entity['tuition_inform'] = ['tuition']

list_entity = [{"major_code": ["112", "108", "114", "125", "441", "245", "223", "109", "115", "123", "228", "128", "206", "237", "141", "207", "219", "242", "214", "106", "107", "129", "117", "140", "120", "145", "209", "208", "266", "138", "137", "210", "215", "142", "220", "225", "110"], "major_name": ["kỹ thuật dệt", "kỹ thuật điện", "kỹ thuật hóa học", "kỹ thuật môi trường", "bảo dưỡng công nghiệp", "kỹ thuật hàng không", "quản lý công nghiệp", "công nghệ may", "công nghệ thực phẩm", "kỹ thuật cơ khí", "công nghệ sinh học", "công nghệ kỹ thuật vật liệu xây dựng", "logistics và quản lý chuỗi cung ứng", "kỹ thuật xây dựng công trình thủy", "kỹ thuật hệ thống công nghiệp", "khoa học máy tính", "vật lý kỹ thuật", "kỹ thuật xây dựng công trình cảng biển", "quản lý tài nguyên môi trường", "kỹ thuật máy tính", "công nghệ kỹ thuật ô tô", "kỹ thuật điện tử viễn thông", "kỹ thuật vật liệu", "kiến trúc", "kỹ thuật nhiệt", "kỹ thuật địa chất", "kỹ thuật tàu thủy", "kỹ thuật trắc địa bản đồ", "kỹ thuật xây dựng cơ sở hạ tầng", "cơ kỹ thuật", "kỹ thuật cơ điện tử", "kỹ thuật xây dựng công trình giao thông", "kỹ thuật dầu khí", "kỹ thuật công trình xây dựng", "kỹ thuật điều khiển và tự động hóa"], "type_edu": ["chính quy", "đại trà", "phân hiệu bến tre", "chất lượng cao", "tiên tiến"], "point": [23.5, 26.75, 24.25, 20.5, 23.75, 78.8, 82.7, 72.5, 70.6, 79.3, 81.8, 700.0, 820.0, 906.0, 926.0, 704.0, 24.0, 21.25, 702.0, 26.25, 26.5, 25.0, 23.0, 25.75, 72.0, 71.9, 927.0, 736.0, 898.0, 75.1, 853.0, 68.4, 762.0, 25.25, 711.0, 73.0, 67.6, 79.6, 77.3, 82.0, 25.5, 703.0, 66.8, 74.9, 82.4, 790.0, 707.0, 855.0, 24.5, 27.5, 76.5, 27.25, 23.25, 71.4, 727.0, 21.0, 26.0, 74.1, 76.9, 84.5, 79.9, 79.0, 71.1, 72.1, 726.0, 27.0, 84.6, 849.0, 837.0, 802.0, 797.0, 83.5, 0.0, 28.0, 79.5, 68.0, 715.0, 81.6, 79.4, 71.2, 791.0, 751.0, 743.0, 897.0], "year": ["2020"], "career": ["quản lý vận hành các dây chuyền sản xuất sợi dệt nhuộm", "quản đốc xưởng sản xuất", "thiết kế thiết bị điện và điện tử công suất", "thiết kế bộ điều khiển máy điện", "thiết kế hệ thống năng lượng tái tạo", "thiết kế mạng điện", "thiết kế trạm biến áp", "thiết kế nhà máy điện", "thiết kế và lập trình giải thuật điều khiển thiết bị và hệ thống điện", "quản lý và vận hành lưới điện", "thiết kế chiếu sáng", "phân tích ổn định thiết bị và nguồn điện", "bảo vệ relay và tự động hóa hệ thống điện", "kỹ thuật cao áp", "vật liệu cách điện", "phân tích dữ liệu khoa học", "phân tích hệ thống", "điều khiển quá trình thời gian thực và lập trình giao tiếp người sử dụng", "quản lý vận hành và vận hành các hệ thống thiết bị công nghệ sản xuất ngành hóa", "nghiên cứu và phát triển sản phẩm", "phân tích và quản lý chất lượng sản phẩm", "tư vấn thiết kế và thi công xây dựng công trình", "cơ sở hạ tầng kỹ thuật liên quan đến vệ sinh môi trường", "tổ chức quản lý bảo dưỡng", "tổ chức quản lý kho", "sửa chữa máy móc", "duy trì sản xuất liên tục và cung cấp dịch vụ bảo trì hậu mãi", "quản lý điều hành hoạt động bảo dưỡng máy bay", "nghiên cứu thiết kế các thiết bị bay", "tư vấn thiết kế cơ khí các hệ thống năng lượng và quy trình sản xuất", "quản lý nhà máy", "hoạch định sản xuất", "quản lý mua hàng và tồn kho", "đánh giá trình độ công nghệ", "quản lý con người", "quản lý mua hàng", "đánh giá các chương trình mua hàng", "thiếp lập cấp độ vận hành và phối hợp các công tác trong vận hành", "định hướng các điểm mấu chốt trong vận hành", "quản lý chất lượng", "phân tích chi tiết cơ sở dữ liệu và các bảng tính", "kiểm định quá trình để xác định các khu vực cần cải tiến", "quản lý việc thực hiện những thay đổi", "lập kế hoạch và quản lý chuỗi cung ứng", "thiết kế trong các dây chuyền sản xuất", "thiết kế kỹ thuật tại các phòng kỹ thuật", "quản lý các dự án về ngành may", "vận hành sản xuất thực phẩm", "kiểm tra chất lượng sản phẩm thực phẩm", "đảm bảo chất lượng sản phẩm thực phẩm", "phân tích chất lượng và an toàn thực phẩm", "thiết kế sản phẩm thực phẩm", "quản lý an toàn thực phẩm", "phụ trách dinh dưỡng thực phẩm", "chế tạo", "điều hành", "sản xuất", "nghiên cứu phát triển", "thiết kế sản phẩm cơ khí", "tư vấn thiết kế", "hệ thống nâng vận chuyển trong hệ thống dây chuyền tự động", "sản xuất vật liệu xây dựng", "sản xuất vật liệu và cấu kiện xây dựng", "máy thi công cơ giới và máy chuyên dụng", "nghiên cứu trong phòng thí nghiệm ở các trường đại học các cơ quan pháp y các trung tâm và viện nghiên cứu", "xây dựng quy trình sản xuất cũng như quản lý điều hành và kiểm soát quá trình sản xuất các sản phẩm công nghệ sinh học ở các qui mô khác nhau", "xây dựng và thực hiện các dự án liên quan đến xử lý ô nhiễm môi trường sống", "giám sát và kiểm tra chất lượng vật liệu xây dựng", "kiểm định chất lượng của toàn bộ công trình xây dựng", "giám sát chất lượng sản xuất sản phẩm", "quản lý và điều hành hệ thống sản xuất hay dịch vụ", "quản lý vật tư và hoạch định tồn kho", "các kỹ thuật tối ưu hóa nguồn lực sản xuất", "kỹ thuật hỗ trợ ra quyết định", "quản lý và kiểm soát chất lượng", "logistics và chuỗi cung ứng", "kỹ thuật điều độ nguồn lực", "thiết kế hệ thống thông tin", "thiết kế và áp dụng hệ thống sản xuất tinh gọn cho tổ chức", "thiết kế thi công và quản lý các công trình chuyên ngành xây dựng các công trình thủy lợi thủy điện", "thiết kế xây dựng các phần mềm máy tính", "thiết kế xây dựng các ứng dụng cho thiết bị di động", "ứng dụng thương mại điện tử trên nền web", "quản trị và xây dựng các giải pháp đảm bảo an toàn cho các hệ thống máy tính và hệ thống mạng máy tính", "tư vấn thẩm định và phát triển các dự án giải pháp công nghệ thông tin", "kỹ sư lâm sàng", "chuyên gia thiết bị y tế", "kinh doanh và sản xuất thiết bị y tế thiết bị trong lĩnh vực công nghệ sinh học công nghệ môi trường", "thiết kế", "thi công", "giám sát", "quản lý dự án", "xây dựng cảng", "công trình biển", "công trình dầu khí", "công trình giao thông", "quản lý các sở ban ngành xây dựng giao thông thuỷ lợi nông nghiệp", "ban quản lý các cảng", "ban quản lý các dự án đường thuỷ", "ban quản lý các chương trình tôn tạo bảo vệ bờ biển hải đảo", "các chương trình ứng phó biến đổi khí hậu nước biển dâng", "quản lý dự án các doanh nghiệp sản xuất các khu công nghiệp", "tư vấn môi trường", "quản lý tài nguyên môi trường", "ban quản lý cải thiện vệ sinh môi trường các lưu vực thoát nước", "cải tạo chất lượng nước trong lưu vực sông", "quản lý chất thải rắn", "lập báo cáo đánh giá tác động môi trường", "thiết kế và xây dựng các phầm mềm phần cứng cho các thiết bị điều khiển tự động", "quản trị và xây dựng các giải pháp đảm bảo an toàn cho các hệ thống máy tính và mạng máy tính", "tư vấn và chuyển giao công nghệ lĩnh vực ô tô và giao thông vận tải đường bộ", "công nghiệp sản xuất và lắp ráp ô tô", "vận hành quản lý khai thác và thiết kế các mạng điện thoại cố định và di động mạng truyền dẫn quang viba thông tin vệ tinh phát thanh truyền hình mạng thông tin dữ liệu", "phân tích và thiết kế các thiết bị thu phát cao tần các vi mạch số và vi mạch tương tự", "vận hành máy móc trong nhà máy chế tạo linh kiện bán dẫn", "lập trình và thiết kế phần cứng xử lý tín hiệu âm thanh hình ảnh và tín hiệu đa phương tiện", "sản xuất gia công vật liệu", "chế tạo vật tư và thiết bị dân dụng thiết bị công nghiệp", "sản xuất phụ tùng thay thế cho các thiết bị công nông ngư nghiệp", "sản xuất các cấu kiện vật liệu xây dựng vật liệu trang trí nội thất", "quản lý và kiểm định chất lượng nguyên vật liệu", "thiết kế kiến trúc nội thất và đô thị", "thiết kế môi trường", "xây dựng quản lý và phát triển bất động sản", "quản lý vận hành bảo trì các nhà máy xí nghiệp sử dụng nhiệt năng", "sản xuất kinh doanh các thiết bị nhiệt lạnh", "nghiên cứu tiết kiệm năng lượng và năng lượng tái tạo", "thí nghiệm đất đá", "tư vấn xây dựng", "xử lý nền móng", "khoan khảo sát địa chất", "thiết kế vật liệu địa kỹ thuật", "khai thác nước", "gia cố nền đất", "xử lý địa chất động lực công trình", "quy hoạch và điều tra tài nguyên nước dưới đất", "quản lý môi trường", "đánh giá tác động môi trường", "cải tạo môi trường địa chất", "khai thác và bảo vệ tài nguyên dầu khí", "khai thác thăm dò khoáng sản", "điều hành mỏ trong các mỏ khai thác", "quản lý điều hành thiết kế tư vấn trong lĩnh vực tàu thủy", "chuyển giao công nghệ liên quan đến tàu thủy", "lập bản đồ địa hình địa chính", "xây dựng và quản lý", "bố trí các công trình nhà cao tầng cầu hầm", "xây dựng hệ thông tin địa lý và quản lý đất đai", "thiết kế thi công và quản lý các công trình chuyên ngành xây dựng cấp thoát nước cho khu quy hoạch", "tư vấn thiết kế thi công hệ thống cấp thoát nước", "hạ tầng kỹ thuật công trình dân dụng công nghiệp các khu đô thị mới", "mô phỏng các bài toán thuộc lĩnh vực cơ học trong kỹ thuật", "lập trình điều khiển máy bằng chương trình số", "thiết kế hệ thống kỹ thuật nhà máy", "quản lý điều hành giải pháp tự động hóa sử dụng hệ thống và sản phẩm cơ điện tử", "tư vấn", "phản biện các vấn đề kỹ thuật xây dựng", "khảo sát", "thiết kế các công trình", "tổ chức và quản lý thi công", "xây dựng công trình cầu đường", "giải quyết các vấn đề về giao thông", "hệ thống giao thông thông minh", "tổ chức giao thông trong các khu đô thị mới", "khoan khai thác tại hiện trường", "đo vẽ bản đồ", "phân tích đánh giá tầng chứa", "tính trữ lượng dầu khí", "khoan khai thác và công nghệ dầu khí", "lập trình trong kỹ thuật dầu khí", "quản lý thi công", "thẩm tra thiết kế", "quản lý dự án xây dựng", "khảo sát và kiểm định công trình", "thiết kế và xây dựng hệ thống đo lường", "điều khiển tự động", "giám sát các hệ thống trong dầu khí", "chế biến thức ăn nước uống", "máy móc", "dược", "phân phối và quản lý năng lượng"], "subject": ["toán", "vật lý", "tiếng anh", "hóa học", "ngữ văn", "sinh học", "vẽ hình họa mỹ thuật"], "tuition": ["5.850.000", "30.000.000"], "subject_group": ["a01", "a1", "a00", "a", "d07", "d7", "d01", "d1", "b00", "b", "v00", "v", "v01", "v1"], "case": ["thi tốt nghiệp trung học phổ thông", "ưu tiên xét tuyển", "đánh giá năng lực"], "criteria": [90, 670, 320, 120, 0, 40, 300, 645, 100, 45, 165, 55, 50, 200, 240, 220, 75, 80, 130, 60, 150, 105], "object": ["thi tốt nghiệp thpt năm 2021", "học sinh các trường chuyên và năng khiếu", "học sinh giỏi 2 năm trở lên", "học sinh giỏi 3 năm trở lên", "thành viên đội tuyển tham dự học sinh giỏi quốc gia", "hạnh kiểm tốt trong 3 năm", "áp dụng một lần đúng năm học sinh tốt nghiệp thpt", "thi đánh giá năng lực đhqg-tphcm"], "register": ["đăng ký dự thi kỳ thi tốt nghiệp thpt 2021", "đăng ký xét tuyển", "đăng ký ưu tiên xét tuyển", "tối đa 03 nguyện vọng", "có phân biệt số thứ tự nguyện vọng"]}]
