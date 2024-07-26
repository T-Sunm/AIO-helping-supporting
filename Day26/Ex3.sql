SELECT 
    Id,
    Name,
    Email,
    Phone,
    Address,
    CreatedDate,
    IF(Gender = 0, 'Nữ', 'Nam') AS Gender,
    BirthDay,
    TIMESTAMPDIFF(YEAR, BirthDay, CURDATE()) AS Age
FROM
    customer