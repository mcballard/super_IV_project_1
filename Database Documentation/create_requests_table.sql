

create table project_one_sandbox.reimbursement_requests(
	reimbursement_request_id serial primary key,
	employee_id int,
	reason_id int,
	amount float check (1 <= amount) check (amount <= 1000),
	constraint employeefk foreign key (employee_id) references project_one_sandbox.employees(employee_id),
	constraint reasonfk foreign key (reason_id) references project_one_sandbox.reasons_table(reason_id) on delete cascade
);
