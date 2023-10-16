from kafi.storage import Storage

# Constants

ALL_MESSAGES = -1

#

class Kafka(Storage):
    def __init__(self, config_dir_str, config_name_str, mandatory_section_str_list, optional_section_str_list):
        super().__init__(config_dir_str, config_name_str, mandatory_section_str_list, optional_section_str_list)
        #
        self.config_dir_str = config_dir_str
        self.config_name_str = config_name_str
        #
        if "kafka" in mandatory_section_str_list:
            self.kafka_config_dict = self.config_dict["kafka"]
        else:
            self.kafka_config_dict = None
        #
        if "rest_proxy" in mandatory_section_str_list:
            self.rest_proxy_config_dict = self.config_dict["rest_proxy"]
        else:
            self.rest_proxy_config_dict = None
        #
        self.admin = None
        #
        # cluster config kafi section
        #
        if "flush.num.messages" not in self.kafi_config_dict:
            self.flush_num_messages(10000)
        else:
            self.flush_num_messages(int(self.kafi_config_dict["flush.num.messages"]))
        #
        if "flush.timeout" not in self.kafi_config_dict:
            self.flush_timeout(-1.0)
        else:
            self.flush_timeout(float(self.kafi_config_dict["flush.timeout"]))
        #
        if "retention.ms" not in self.kafi_config_dict:
            self.retention_ms(604800000)
        else:
            self.retention_ms(int(self.kafi_config_dict["retention.ms"]))
        #
        if "consume.timeout" not in self.kafi_config_dict:
            self.consume_timeout(5.0)
        else:
            self.consume_timeout(float(self.kafi_config_dict["consume.timeout"]))
        #
        if "enable.auto.commit" not in self.kafi_config_dict:
            self.enable_auto_commit(True)
        else:
            self.enable_auto_commit(bool(self.kafi_config_dict["enable.auto.commit"]))
        #
        if "session.timeout.ms" not in self.kafi_config_dict:
            self.session_timeout_ms(45000)
        else:
            self.session_timeout_ms(int(self.kafi_config_dict["session.timeout.ms"]))
        #
        if "block.num.retries" not in self.kafi_config_dict:
            self.block_num_retries(10)
        else:
            self.block_num_retries(int(self.kafi_config_dict["block.num.retries"]))
        #
        if "block.interval" not in self.kafi_config_dict:
            self.block_interval(0.5)
        else:
            self.block_interval(float(self.kafi_config_dict["block.interval"]))
        #
        # both cluster and restproxy kafi section
        #
        if "fetch.min.bytes" not in self.kafi_config_dict:
            self.fetch_min_bytes(-1)
        else:
            self.fetch_min_bytes(int(self.kafi_config_dict["fetch.min.bytes"]))
        #
        if "consumer.request.timeout.ms" not in self.kafi_config_dict:
            self.consumer_request_timeout_ms(1000)
        else:
            self.consumer_request_timeout_ms(int(self.kafi_config_dict["consumer.request.timeout.ms"]))
        #
        if "consume.num.attempts" not in self.kafi_config_dict:
            self.consume_num_attempts(3)
        else:
            self.consume_num_attempts(int(self.kafi_config_dict["consume.num.attempts"]))
        #
        if "requests.num.retries" not in self.kafi_config_dict:
            self.requests_num_retries(10)
        else:
            self.requests_num_retries(int(self.kafi_config_dict["requests.num.retries"]))

    #

    def flush_num_messages(self, new_value=None): # int
        return self.get_set_config("flush.num.messages", new_value)

    def flush_timeout(self, new_value=None): # float
        return self.get_set_config("flush.timeout", new_value)

    def retention_ms(self, new_value=None): # int
        return self.get_set_config("retention.ms", new_value)

    def consume_timeout(self, new_value=None): # float
        return self.get_set_config("consume.timeout", new_value)

    def enable_auto_commit(self, new_value=None): # bool
        return self.get_set_config("enable.auto.commit", new_value)

    def session_timeout_ms(self, new_value=None): # int
        return self.get_set_config("session.timeout.ms", new_value)

    def block_num_retries(self, new_value=None): # int
        return self.get_set_config("block.num.retries", new_value)

    def block_interval(self, new_value=None): # float
        return self.get_set_config("block.interval", new_value)

    #

    def fetch_min_bytes(self, new_value=None): # int
        return self.get_set_config("fetch.min.bytes", new_value)

    def consumer_request_timeout_ms(self, new_value=None): # int
        return self.get_set_config("consumer.request.timeout.ms", new_value)

    def consume_num_attempts(self, new_value=None): # int
        return self.get_set_config("consume.num.attempts", new_value)

    def requests_num_retries(self, new_value=None): # int
        return self.get_set_config("requests.num.retries", new_value)

    #

    def topics(self, pattern=None, size=False, **kwargs):
        return self.admin.topics(pattern, size, **kwargs)
    
    ls = topics

    def l(self, pattern=None, size=True, **kwargs):
        return self.admin.topics(pattern=pattern, size=size, **kwargs)

    ll = l

    def exists(self, topic):
        topic_str = topic
        #
        return self.admin.topics(topic_str) != []
    
    # Topics

    def watermarks(self, pattern, **kwargs):
        return self.admin.watermarks(pattern, **kwargs)

    def config(self, pattern):
        return self.admin.config(pattern)

    def set_config(self, pattern, config, **kwargs):
        return self.admin.set_config(pattern, config, **kwargs)
    
    def create(self, topic, partitions=1, config={}, **kwargs):
        return self.admin.create(topic, partitions, config, **kwargs)
    
    touch = create

    def delete(self, pattern, **kwargs):
        return self.admin.delete(pattern, **kwargs)

    rm = delete

    def offsets_for_times(self, pattern, partitions_timestamps, **kwargs):
        return self.admin.offsets_for_times(pattern, partitions_timestamps, **kwargs)
    
    def partitions(self, pattern=None, verbose=False):
        return self.admin.partitions(pattern, verbose)

    def set_partitions(self, pattern, num_partitions, **kwargs):
        return self.admin.set_partitions(pattern, num_partitions, **kwargs)
    
    def list_topics(self, pattern):
        return self.admin.list_topics(pattern)

    # Groups

    def groups(self, pattern="*", state_pattern="*", state=False):
        return self.admin.groups(pattern, state_pattern, state)
    
    def describe_groups(self, pattern="*", state_pattern="*"):
        return self.admin.describe_groups(pattern, state_pattern)
    
    def delete_groups(self, pattern, state_pattern="*"):
        return self.admin.delete_groups(pattern, state_pattern)
    
    def group_offsets(self, pattern, state_pattern="*"):
        return self.admin.group_offsets(pattern, state_pattern)

    def set_group_offsets(self, group_offsets):
        return self.admin.set_group_offsets(group_offsets)

    # Brokers

    def brokers(self, pattern=None):
        return self.admin.brokers(pattern)
    
    def broker_config(self, pattern=None):
        return self.admin.broker_config(pattern)
    
    def set_broker_config(self, pattern, config, **kwargs):
        return self.admin.set_broker_config(pattern, config, **kwargs)

    # ACLs

    def acls(self, restype="any", name=None, resource_pattern_type="any", principal=None, host=None, operation="any", permission_type="any"):
        return self.admin.acls(restype, name, resource_pattern_type, principal, host, operation, permission_type)

    def create_acl(self, restype="any", name=None, resource_pattern_type="any", principal=None, host=None, operation="any", permission_type="any"):
        return self.admin.create_acl(restype, name, resource_pattern_type, principal, host, operation, permission_type)
    
    def delete_acl(self, restype="any", name=None, resource_pattern_type="any", principal=None, host=None, operation="any", permission_type="any"):
        return self.admin.delete_acl(restype, name, resource_pattern_type, principal, host, operation, permission_type)

    # Open
    def consumer(self, topics, **kwargs):
        consumer = self.get_consumer(topics, **kwargs)
        #
        return consumer
        
    def producer(self, topic, **kwargs):
        producer = self.get_producer(topic, **kwargs)
        #
        return producer
