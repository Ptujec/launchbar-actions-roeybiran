from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_male = (
        '{{first_name_male}} {{last_name}}',
    )
    formats_female = (
        '{{first_name_female}} {{last_name}}',
    )

    formats = formats_male + formats_female

    # Source: 2012 Voters List.
    # Obtained from http://mashasada.me/en/chamotvirtva
    first_names_male = (
        'ავთანდილ', 'აკაკი', 'ალექს', 'ალექსანდრე', 'ამირან', 'ანზორ', 'არმენ',
        'არტურ', 'არჩილ', 'ასლან', 'ბადრი', 'ბესარიონ', 'ბესიკ', 'ბექა',
        'ბიძინა', 'ბონდო', 'ბორის', 'გელა', 'გენადი', 'გია', 'გიგა', 'გიგლა',
        'გივი', 'გიორგი', 'გოგა', 'გოგი', 'გოგიტა', 'გოდერძი', 'გოჩა', 'გრიგოლ',
        'გურამ', 'დავით', 'დათო', 'დემურ', 'დიმიტრი', 'ედუარდ', 'ელგუჯა',
        'ემზარ', 'ვალერი', 'ვალერიან', 'ვანო', 'ვაჟა', 'ვასილ', 'ვახტანგ',
        'ვახტანგ', 'ვეფხვია', 'ვიქტორ', 'ვლადიმერ', 'ზაზა', 'ზაურ', 'ზაქარია',
        'ზვიად', 'ზურაბ', 'თამაზ', 'თეიმურაზ', 'თემურ', 'თენგიზ', 'თორნიკე',
        'იაგო', 'ივანე', 'ილია', 'იოსებ', 'ირაკლი', 'იური', 'კარლო', 'კახა',
        'კახაბერ', 'კობა', 'კონსტანტინე', 'ლაშა', 'ლევან', 'მალხაზ', 'მამუკა',
        'მერაბ', 'მინდია', 'მირიან', 'მიხეილ', 'მიხეილ', 'მურთაზ', 'მურმან',
        'ნიკა', 'ნიკოლოზ', 'ნოდარ', 'ნუგზარ', 'ნუკრი', 'ოთარ', 'ომარ', 'პაატა',
        'პავლე', 'პეტრე', 'რამაზ', 'რატი', 'რევაზ', 'რეზო', 'რობერტ', 'როინ',
        'როლანდ', 'რომან', 'სერგო', 'სიმონ', 'სოსო', 'ტარიელ', 'უშანგი', 'უჩა',
        'შალვა', 'შაქრო', 'შოთა', 'ხვიჩა', 'ჯაბა', 'ჯემალ', 'ჯონი', 'ჯუმბერ',
    )

    # Source: 2012 Voters List.
    # Obtained from http://mashasada.me/en/chamotvirtva
    first_names_female = (
        'აზა', 'აიდა', 'ალა', 'ანა', 'ანი', 'ანიკო', 'ანნა', 'ანჟელა', 'ასმათ',
        'ბელა', 'გალინა', 'გვანცა', 'გიული', 'გუგული', 'გულიკო', 'გულნარა',
        'დალი', 'დარეჯან', 'დიანა', 'დოდო', 'ევგენია', 'ეთერ', 'ეკა',
        'ეკატერინე', 'ელენა', 'ელენე', 'ელზა', 'ელიზა', 'ელისო', 'ელმირა',
        'ემა', 'ვალენტინა', 'ვარდო', 'ვენერა', 'ვერა', 'ვერიკო', 'ვიოლეტა',
        'ზაირა', 'ზინა', 'ზოია', 'თათია', 'თამარ', 'თამარა', 'თამარი', 'თამთა',
        'თამილა', 'თამუნა', 'თეა', 'თეონა', 'თინა', 'თინათინ', 'ია', 'იამზე',
        'იზა', 'იზოლდა', 'ინგა', 'ინეზა', 'ირინა', 'ირინე', 'ირმა', 'კარინე',
        'კლარა', 'ლალი', 'ლამარა', 'ლამზირა', 'ლანა', 'ლარისა', 'ლეილა', 'ლელა',
        'ლენა', 'ლია', 'ლიანა', 'ლიდა', 'ლიზა', 'ლიკა', 'ლილი', 'ლუბა',
        'ლუდმილა', 'ლუიზა', 'მაგდა', 'მადონა', 'მაია', 'მაკა', 'მანანა',
        'მარგალიტა', 'მარი', 'მარია', 'მარიამ', 'მარიკა', 'მარინა', 'მარინე',
        'მარო', 'მაყვალა', 'მეგი', 'მედეა', 'მედიკო', 'მერი', 'მზია',
        'მთვარისა', 'მირანდა', 'ნადეჯდა', 'ნადია', 'ნაზი', 'ნაზიბროლა',
        'ნაზიკო', 'ნათელა', 'ნათია', 'ნაირა', 'ნანა', 'ნანი', 'ნანული',
        'ნარგიზა', 'ნატალია', 'ნატო', 'ნელი', 'ნესტან', 'ნინელი', 'ნინო',
        'ნონა', 'ნორა', 'ნუნუ', 'ნუცა', 'ოლია', 'ოლღა', 'ჟანა', 'ჟენია',
        'ჟუჟუნა', 'რიმა', 'რიტა', 'როზა', 'რუსუდან', 'რუსუდან', 'სალომე',
        'სვეტლანა', 'სონია', 'სოფია', 'სოფიკო', 'სოფიო', 'სულიკო', 'სუსანა',
        'ტატიანა', 'ფატი', 'ფატიმა', 'ფიქრია', 'ქეთევან', 'ქეთინო', 'ქეთო',
        'ქრისტინე', 'შორენა', 'ციალა', 'ცირა', 'ცისანა', 'ციური', 'ციცინო',
        'ხათუნა', 'ხატია', 'ჯულიეტა',
    )

    first_names = first_names_male + first_names_female

    # Source: 2012 Voters List.
    # Obtained from http://mashasada.me/en/chamotvirtva
    last_names = (
        'აბაშიძე', 'აბდულაევი', 'აბესაძე', 'აბრამიშვილი', 'აბულაძე', 'ადამია',
        'ადეიშვილი', 'ადუაშვილი', 'ავალიანი', 'ალადაშვილი', 'ალანია', 'ალიევა',
        'ალიევი', 'ანდღულაძე', 'ანთაძე', 'არაბიძე', 'არაბული', 'არველაძე',
        'არჩვაძე', 'ასათიანი', 'ასანიძე', 'აფციაური', 'ახალაია', 'ახალაძე',
        'ახვლედიანი', 'ახობაძე', 'ბაკურაძე', 'ბალიაშვილი', 'ბარამიძე',
        'ბარბაქაძე', 'ბასილაშვილი', 'ბასილაძე', 'ბაქრაძე', 'ბახტაძე',
        'ბეგიაშვილი', 'ბენდელიანი', 'ბენიძე', 'ბეჟანიშვილი', 'ბეჟანიძე',
        'ბერაია', 'ბერაძე', 'ბერიანიძე', 'ბერიაშვილი', 'ბერიშვილი', 'ბერიძე',
        'ბერუაშვილი', 'ბერულავა', 'ბერძენიშვილი', 'ბექაური', 'ბიბილაშვილი',
        'ბიგვავა', 'ბიწაძე', 'ბლიაძე', 'ბოკუჩავა', 'ბოლქვაძე', 'ბოჭორიშვილი',
        'ბრეგაძე', 'ბრეგვაძე', 'ბუკია', 'ბურდული', 'ბურჯანაძე', 'ბუჩუკური',
        'ბუცხრიკიძე', 'გაბაიძე', 'გაბედავა', 'გაბელია', 'გაბრიჭიძე', 'გაბუნია',
        'გაგნიძე', 'გაგუა', 'გაფრინდაშვილი', 'გაჩეჩილაძე', 'გაჯიევა', 'გაჯიევი',
        'გეგეშიძე', 'გელაშვილი', 'გელაძე', 'გვაზავა', 'გვასალია', 'გველესიანი',
        'გვენეტაძე', 'გიგაური', 'გიორგაძე', 'გიორგობიანი', 'გობეჯიშვილი',
        'გოგალაძე', 'გოგია', 'გოგიაშვილი', 'გოგინაშვილი', 'გოგიტიძე',
        'გოგიშვილი', 'გოგიჩაიშვილი', 'გოგიჩაშვილი', 'გოგიძე', 'გოგოლაძე',
        'გოგოხია', 'გოგსაძე', 'გოგუა', 'გოგუაძე', 'გორგაძე', 'გორგილაძე',
        'გორგოძე', 'გოცირიძე', 'გრიგალაშვილი', 'გრიგორიანი', 'გრძელიშვილი',
        'გულიაშვილი', 'გულუა', 'გუმბერიძე', 'გურგენიძე', 'გურეშიძე', 'გურული',
        'გუჯაბიძე', 'დავითაშვილი', 'დავითაძე', 'დალაქიშვილი', 'დანელია',
        'დარბაიძე', 'დევაძე', 'დევიძე', 'დემეტრაშვილი', 'დვალი', 'დვალიშვილი',
        'დიასამიძე', 'დოლიძე', 'დუმბაძე', 'ელბაქიძე', 'ელიზბარაშვილი',
        'ენუქიძე', 'ვალიევა', 'ვალიევი', 'ვარდოსანიძე', 'ვარშანიძე', 'ვასაძე',
        'ვაშაკიძე', 'ვაშაყმაძე', 'ვეკუა', 'ზარანდია', 'ზარიძე', 'ზარქუა',
        'ზედგინიძე', 'ზოიძე', 'ზურაბაშვილი', 'თაბაგარი', 'თავართქილაძე',
        'თავაძე', 'თედორაძე', 'თევზაძე', 'თოდუა', 'თოლორდავა', 'თოფურია',
        'თურმანიძე', 'იაშვილი', 'ილურიძე', 'იმერლიშვილი', 'იმნაძე', 'ინასარიძე',
        'იობიძე', 'ირემაშვილი', 'ირემაძე', 'ისაევი', 'კაზარიანი', 'კაკაბაძე',
        'კაკაურიძე', 'კაკულია', 'კალანდაძე', 'კალანდია', 'კანდელაკი',
        'კაპანაძე', 'კარაპეტიანი', 'კაცაძე', 'კაციტაძე', 'კაჭარავა', 'კახაძე',
        'კახიძე', 'კევლიშვილი', 'კეკელიძე', 'კერესელიძე', 'კვანტალიანი',
        'კვარაცხელია', 'კვაჭაძე', 'კვერნაძე', 'კვინიკაძე', 'კვირიკაშვილი',
        'კვირკველია', 'კიკვაძე', 'კიკნაძე', 'კილასონია', 'კილაძე',
        'კინწურაშვილი', 'კირვალიძე', 'კირთაძე', 'კირკიტაძე', 'კობაიძე',
        'კობახიძე', 'კობერიძე', 'კობიაშვილი', 'კონცელიძე', 'კოპალიანი',
        'კოპაძე', 'კოხრეიძე', 'კუბლაშვილი', 'კუპატაძე', 'კუპრაშვილი',
        'კუპრეიშვილი', 'კურტანიძე', 'კუჭავა', 'კუჭუხიძე', 'კუხიანიძე', 'ლაბაძე',
        'ლაგვილავა', 'ლატარია', 'ლაცაბიძე', 'ლეჟავა', 'ლიპარტელიანი',
        'ლობჟანიძე', 'ლობჯანიძე', 'ლოლაძე', 'ლომაძე', 'ლომთაძე', 'ლომიძე',
        'ლომსაძე', 'ლორთქიფანიძე', 'ლურსმანაშვილი', 'მაზმიშვილი', 'მათიაშვილი',
        'მაისურაძე', 'მამალაძე', 'მამულაშვილი', 'მამულაძე', 'მანაგაძე',
        'მარგველაშვილი', 'მაღლაკელიძე', 'მაღრაძე', 'მაჩიტიძე', 'მაჭავარიანი',
        'მაჭარაშვილი', 'მახათაძე', 'მახარაშვილი', 'მახარაძე', 'მგალობლიშვილი',
        'მგელაძე', 'მეგრელიშვილი', 'მელაძე', 'მელიქიშვილი', 'მელიქიძე',
        'მელქაძე', 'მერაბიშვილი', 'მერებაშვილი', 'მესხი', 'მეტრეველი',
        'მეფარიშვილი', 'მიმინოშვილი', 'მინდიაშვილი', 'მიქაბერიძე', 'მიქავა',
        'მიქაძე', 'მიქელაძე', 'მოდებაძე', 'მოსიაშვილი', 'მჟავანაძე', 'მუმლაძე',
        'მუსაევა', 'მუსაევი', 'მუსტაფაევა', 'მუსტაფაევი', 'მუშკუდიანი',
        'მღებრიშვილი', 'მჭედლიშვილი', 'მჭედლიძე', 'ნაბიევი', 'ნადირაშვილი',
        'ნადირაძე', 'ნაკაშიძე', 'ნარიმანიძე', 'ნასყიდაშვილი', 'ნატროშვილი',
        'ნაცვლიშვილი', 'ნაჭყებია', 'ნებიერიძე', 'ნემსაძე', 'ნეფარიძე',
        'ნიკოლაიშვილი', 'ნიკოლეიშვილი', 'ნიჟარაძე', 'ნიქაბაძე', 'ნოზაძე',
        'ნუცუბიძე', 'ოთარაშვილი', 'ონიანი', 'ოქროპირიძე', 'ოქრუაშვილი',
        'პავლიაშვილი', 'პაპავა', 'პაპაშვილი', 'პაპიაშვილი', 'პაპიძე',
        'პაპუაშვილი', 'პატარაია', 'პეტრიაშვილი', 'პეტროსიანი', 'ჟვანია',
        'ჟორჟოლიანი', 'ჟღენტი', 'რაზმაძე', 'რამიშვილი', 'რევაზიშვილი',
        'რეხვიაშვილი', 'რობაქიძე', 'როგავა', 'როსტიაშვილი', 'რუხაძე',
        'სალუქვაძე', 'სამუშია', 'სამხარაძე', 'სანიკიძე', 'სარალიძე',
        'სარქისიანი', 'საჯაია', 'სეხნიაშვილი', 'სვანიძე', 'სილაგაძე',
        'სიმონიშვილი', 'სირაძე', 'სირბილაძე', 'სიჭინავა', 'სიხარულიძე',
        'სოფრომაძე', 'სულაბერიძე', 'სურმანიძე', 'სხირტლაძე', 'ტაბატაძე',
        'ტაკიძე', 'ტალახაძე', 'ტურაშვილი', 'ტუღუში', 'ტყებუჩავა', 'ტყემალაძე',
        'ტყეშელაშვილი', 'უგრეხელიძე', 'ურუშაძე', 'ფანცულაია', 'ფარტენაძე',
        'ფარცვანია', 'ფეიქრიშვილი', 'ფერაძე', 'ფირცხალავა', 'ფიფია',
        'ფიცხელაური', 'ფოფხაძე', 'ფუტკარაძე', 'ფხაკაძე', 'ფხალაძე', 'ქავთარაძე',
        'ქათამაძე', 'ქამადაძე', 'ქანთარია', 'ქარდავა', 'ქართველიშვილი',
        'ქარჩავა', 'ქარცივაძე', 'ქაჯაია', 'ქევხიშვილი', 'ქირია', 'ქობალია',
        'ქობულაძე', 'ქორიძე', 'ქუთათელაძე', 'ქურდაძე', 'ღამბაშიძე',
        'ღარიბაშვილი', 'ღვინიაშვილი', 'ღვინჯილია', 'ღლონტი', 'ღონღაძე',
        'ღურწკაია', 'ყაველაშვილი', 'ყიფიანი', 'ყიფშიძე', 'ყოლბაია', 'ყურაშვილი',
        'შავაძე', 'შათირიშვილი', 'შაინიძე', 'შალამბერიძე', 'შამათავა',
        'შამუგია', 'შანიძე', 'შარაშიძე', 'შარიქაძე', 'შელია', 'შენგელია',
        'შეყილაძე', 'შველიძე', 'შონია', 'შუბითიძე', 'შუკაკიძე', 'ჩადუნელი',
        'ჩაკვეტაძე', 'ჩაფიძე', 'ჩაჩანიძე', 'ჩაჩუა', 'ჩინჩალაძე', 'ჩიქოვანი',
        'ჩიხლაძე', 'ჩოხელი', 'ჩუბინიძე', 'ჩხაიძე', 'ჩხარტიშვილი', 'ჩხეიძე',
        'ჩხიკვაძე', 'ცაავა', 'ცანავა', 'ცარციძე', 'ცერცვაძე', 'ცეცხლაძე',
        'ცინცაძე', 'ცირეკიძე', 'ცომაია', 'ცუცქირიძე', 'ცხადაძე', 'ძიძიგური',
        'ძნელაძე', 'წერეთელი', 'წიკლაური', 'წიქარიშვილი', 'წულაია', 'წულუკიძე',
        'წურწუმია', 'ჭანტურია', 'ჭანტურიძე', 'ჭაღალიძე', 'ჭეიშვილი', 'ჭელიძე',
        'ჭითანავა', 'ჭინჭარაული', 'ჭიღლაძე', 'ჭიჭინაძე', 'ჭკადუა', 'ჭუმბურიძე',
        'ხალვაში', 'ხარაბაძე', 'ხარაზიშვილი', 'ხარაიშვილი', 'ხარატიშვილი',
        'ხარებავა', 'ხარშილაძე', 'ხარჩილავა', 'ხატიაშვილი', 'ხაჩატურიანი',
        'ხაჩიძე', 'ხაჭაპურიძე', 'ხელაძე', 'ხეცურიანი', 'ხვედელიძე', 'ხვიჩია',
        'ხიზანიშვილი', 'ხიმშიაშვილი', 'ხმალაძე', 'ხოზრევანიძე', 'ხორავა',
        'ხურცილავა', 'ხურციძე', 'ხუციშვილი', 'ჯავახიშვილი', 'ჯაიანი',
        'ჯალაღონია', 'ჯანაშია', 'ჯანელიძე', 'ჯანიაშვილი', 'ჯანჯღავა',
        'ჯაფარიძე', 'ჯიბლაძე', 'ჯინჭარაძე', 'ჯიქია', 'ჯიშკარიანი', 'ჯოხაძე',
        'ჯოჯუა', 'ჯღარკავა',
    )